# Workflow: Meeting Notes & Action Items

## Purpose

Turn transcripts or pasted notes into structured summaries, decisions, action items, and open questions.

## When to use

- after meetings
- after calls or long discussions
- when action items should not remain buried in chat

## Inputs

- transcript text or transcript file
- optional attendee list or team mapping

## Outputs

- concise summary
- decisions list
- action items with owners and deadlines where possible
- open questions

## Procedure

1. Start with pasted transcript or local file input.
2. Summarize key topics and decisions.
3. Extract action items with owner + deadline if present.
4. Save the result as a local note first.
5. Only after output quality is proven, connect external task systems.

## Verification

- summary is concise
- action items are explicit and not hidden in prose
- unknown owner/deadline fields are marked clearly, not hallucinated

## Risks / gotchas

- auto-creating external tasks too early can create noisy systems
- speaker attribution may be imperfect in low-quality transcripts

## Related files

- `templates/meeting-notes-template.md`
