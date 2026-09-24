"""Save deterministic retrieval, chunk, and refusal evidence without model calls.

Run from the repository root: python tools/capture_eval_evidence.py --label after
This supplements run_eval.py; it does not replace the three generation runs.
"""
import argparse
import contextlib
import datetime as dt
import io
import json
from dataclasses import asdict
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import app
import config
import gate
import generate
import questions
from chunker import split_documents
from ingest import load_documents
from store import search


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--label', required=True, choices=['before', 'after'])
    args = parser.parse_args()
    documents = load_documents(config.CORPUS)
    chunks = split_documents(documents)
    current = {c.label: c.text for c in chunks}
    retrieval = []
    for item in questions.answered():
        results = search(item['question'])
        retrieval.append({
            'question': item['question'],
            'results': [asdict(r) for r in results],
            'matches_current_chunks': all(current.get(r.label) == r.text for r in results),
        })
    refusals = []
    for question in questions.OUT_OF_SCOPE:
        results = search(question)
        decision = gate.check(results)
        calls_before = generate.call_count()
        # Never send a gate-accepted question to generation in this collector.
        outcome = app.ask_pipeline(question) if not decision.passed else None
        refusals.append({
            'question': question,
            'gate': asdict(decision),
            'pipeline_output': outcome,
            'model_calls': generate.call_count() - calls_before,
        })
    captured = io.StringIO()
    with contextlib.redirect_stdout(captured):
        app.cmd_chunks(argparse.Namespace(corpus=config.CORPUS, from_doc=None, indices=None, n=5))
    record = {
        'when': dt.datetime.now().isoformat(),
        'corpus': config.CORPUS,
        'top_k': config.TOP_K,
        'threshold': config.THRESHOLD,
        'model': config.MODEL,
        'embedding_model': config.EMBEDDING_MODEL,
        'fake_embeddings': __import__('os').getenv('AI201_FAKE_EMBEDDINGS') == '1',
        'grounding_instruction': generate.GROUNDING_INSTRUCTION,
        'retrieval': retrieval,
        'refusals': refusals,
        'sample_chunks_cli': captured.getvalue(),
        'model_calls': generate.call_count(),
    }
    path = config.RESULTS_DIR / f'unit2_{args.label}_evidence.json'
    path.write_text(json.dumps(record, indent=2, ensure_ascii=False) + '\n')
    sample_path = config.RESULTS_DIR / f'unit2_{args.label}_chunks.txt'
    sample_path.write_text(captured.getvalue())
    print(f'Saved {path.relative_to(config.ROOT)} and {sample_path.relative_to(config.ROOT)}')
    print(f'Collector model calls: {generate.call_count()}')
    print('All retrieved passages match current chunks:', all(r['matches_current_chunks'] for r in retrieval))
    assert not record['fake_embeddings'], 'Evaluation must use real embeddings'
    assert record['model_calls'] == 0, 'Collector must not call the model'
    assert all(r['matches_current_chunks'] for r in retrieval), 'Index differs from current chunks'


if __name__ == '__main__':
    main()
