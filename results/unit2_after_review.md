# Unit 2 after evaluation — manual review

Answers: run_2026-09-23_2035_after.md. Original targets: ../criteria.md.
Reviewed against full retrieved passages in unit2_after_evidence.json.
No automatic scorer was used. Each cell below reports manual judgments for
criterion 2 (source) and criterion 5 (all required facts), not keyword-only checks.

| Question | Required facts checked | Run 1 | Run 2 | Run 3 |
|---|---|---|---|---|
| Housing lottery | Accumulated credit hours before random tie-breaking | Source + facts pass | Source + facts pass | Source + facts pass |
| Aldridge wash | $1.75, card only | Source + facts pass | Source + facts pass | Source + facts pass |
| Meal plan | First ten days, refund to student account | Source + facts pass | Source + facts pass | Source + facts pass |
| Library | Reading week 10pm, term time 2am | Source + facts pass | Source + facts pass | Source + facts pass |
| Pass/fail | C- or better | Source + facts pass | Source + facts pass | Source + facts pass |

Each answer names its correct retrieved source. No contradictory or unsupported
addition was found. Library Run 3 is grammatically awkward ("closes at 2am during
term and until 10pm during reading week"), but the periods and times are correct.
The original criterion judges facts, not prose style, so that answer passes.

Retrieval: the first result for each question contains every required fact;
all 25 passages match the earlier saved retrieval text and current chunk output.
Chunk review: all five printed samples retain the exact source title and whole
source paragraphs; manual reading confirms complete sentences at both boundaries.
Gate: all five actual pipeline outputs have the exact refusal and zero calls.
These deterministic counts are each 5/5, repeated in the run-log columns.

Execution: .venv/bin/python -u run_eval.py --label after

Actual terminal usage output:

```text
15 model calls this session, 9478 tokens (8985 in, 493 out)
```

The collector ran separately and made zero model calls. Its first sandboxed
attempt failed during ONNX setup; the permitted retry completed successfully.
This failure did not alter the completed generation evaluation.
