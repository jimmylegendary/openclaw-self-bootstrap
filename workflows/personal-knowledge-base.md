# Workflow: Personal Knowledge Base

## Purpose

Build a searchable corpus of external materials such as URLs, articles, tweets, PDFs, and transcripts.

## When to use

- when the user saves external resources regularly
- when research needs to be reusable across future tasks

## Inputs

- URL or file to ingest
- optional title, topic, or source metadata

## Outputs

- saved content record with metadata
- searchable research corpus

## Procedure

1. Fetch or import the external content.
2. Save the content or structured summary with metadata.
3. Keep source URL and date.
4. Use the corpus later for question answering and research support.
5. Start with local storage first; add vector search later if needed.

## Verification

- saved items keep source references
- future queries can find earlier saved materials
- the system distinguishes external resources from personal memory

## Risks / gotchas

- raw dumping without metadata becomes hard to reuse
- do not confuse knowledge-base storage with durable personal memory

## Related files

- `sources/awesome-openclaw-usecases.md`
- `workflows/second-brain.md`
