# Milestone 3 — chunk review

Corpus: campus_life. Real ONNX embeddings used for indexing.

Baseline command: `.venv/bin/python -B app.py --corpus campus_life --variant milestone2-baseline index`

```text
88 documents, 27,908 characters, ~317 characters per document
88 chunks, 317 characters on average (shortest 178, longest 549), produced by chunker.py::fallback_split
stored 88 chunks
```

Replacement summary from `chunker.py::describe`:

```text
100 chunks, 282 characters on average (shortest 116, longest 400), produced by chunker.py::split_documents
```

Five sample chunks and the standalone-question review are in README.md.
A local assertion check verified exact reconstruction of all body paragraphs,
original order, retained titles, sequential indices, and unique source labels
for all four supplied corpora. Empty documents, single-paragraph documents,
and oversized paragraphs were also checked. All checks passed. These checks
verify preservation and boundaries, not retrieval quality.

The first replacement index attempt failed because ONNX could not create its
sandboxed temporary working directory. It was rerun with the required filesystem
permission; no fake embeddings were used.
