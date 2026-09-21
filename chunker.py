"""Stage 2: pack complete paragraphs, retaining each source title as context.

The campus_life corpus consists of short titled posts. The custom splitter
uses a soft size target rather than cutting sentences. The original fixed
window splitter remains below for comparison.
"""

from dataclasses import dataclass

import config
from ingest import Document


@dataclass
class Chunk:
    """One piece of one document."""

    text: str
    source: str        # which file it came from
    index: int         # which chunk within that file, starting at 0
    produced_by: str   # the function that made it — cite this in your README

    @property
    def label(self) -> str:
        return f"{self.source}#{self.index}"


def fallback_split(
    documents: list[Document],
    chunk_size: int | None = None,
    overlap: int | None = None,
) -> list[Chunk]:
    """
    The starter's original chunker. Fixed-size character windows with overlap.

    Keep this function. Milestone 3's stop rule points back at it, and having
    something to compare your own strategy against is useful in unit 2.
    """
    chunk_size = chunk_size or config.CHUNK_SIZE
    overlap = overlap or config.CHUNK_OVERLAP

    if overlap >= chunk_size:
        raise ValueError("overlap has to be smaller than chunk_size")

    chunks: list[Chunk] = []
    for doc in documents:
        start = 0
        index = 0
        while start < len(doc.text):
            piece = doc.text[start : start + chunk_size].strip()
            if piece:
                chunks.append(
                    Chunk(
                        text=piece,
                        source=doc.source,
                        index=index,
                        produced_by="chunker.py::fallback_split",
                    )
                )
                index += 1
            start += chunk_size - overlap

    return chunks


def split_documents(documents: list[Document]) -> list[Chunk]:
    """Pack whole paragraphs up to CHUNK_SIZE, repeating the title.

    CHUNK_SIZE includes the title and is a soft limit: an oversized paragraph
    stays intact. Body paragraphs do not overlap. The first paragraph is the
    title in the supplied campus_life posts; untitled one-paragraph documents
    are retained whole instead of producing an empty body chunk.
    """
    if config.CHUNK_SIZE <= 0:
        raise ValueError("CHUNK_SIZE must be positive")
    if config.CHUNK_OVERLAP != 0:
        raise ValueError("The paragraph chunker requires CHUNK_OVERLAP = 0")

    chunks: list[Chunk] = []
    for doc in documents:
        paragraphs = [part.strip() for part in doc.text.split("\n\n") if part.strip()]
        if not paragraphs:
            continue

        title, *body = paragraphs
        pieces: list[str] = []
        current: list[str] = []
        for paragraph in body:
            candidate = "\n\n".join([title, *current, paragraph])
            if current and len(candidate) > config.CHUNK_SIZE:
                pieces.append("\n\n".join([title, *current]))
                current = []
            current.append(paragraph)
        if current:
            pieces.append("\n\n".join([title, *current]))
        elif not body:
            pieces.append(title)

        chunks.extend(
            Chunk(
                text=text,
                source=doc.source,
                index=index,
                produced_by="chunker.py::split_documents",
            )
            for index, text in enumerate(pieces)
        )
    return chunks


def describe(chunks: list[Chunk]) -> str:
    """A one-line summary, printed after indexing."""
    if not chunks:
        return "0 chunks"
    lengths = [len(c.text) for c in chunks]
    return (
        f"{len(chunks)} chunks, "
        f"{sum(lengths) // len(lengths)} characters on average "
        f"(shortest {min(lengths)}, longest {max(lengths)}), "
        f"produced by {chunks[0].produced_by}"
    )


if __name__ == "__main__":
    from ingest import load_documents

    chunks = split_documents(load_documents())
    print(describe(chunks))
