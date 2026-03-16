# Workflow: arXiv Paper Reader

## Purpose

Read, triage, summarize, and compare arXiv papers conversationally.

## When to use

- research workflows
- reading list triage
- paper comparison and section-level explanation

## Inputs

- one or more arXiv IDs
- optional research topic or relevance criteria

## Outputs

- abstract summaries
- section map
- paper comparisons
- key takeaways

## Procedure

1. Start with abstracts before full-paper retrieval.
2. If relevant, fetch the full paper and exclude appendix by default when appropriate.
3. Summarize contributions, methodology, and results.
4. Keep a running reading log for papers already processed.
5. Compare multiple papers by topic relevance when needed.

## Verification

- abstracts are checked before deeper reading
- section-specific requests are grounded in the paper structure
- takeaways are stored for later reuse

## Risks / gotchas

- paper summaries can flatten nuance if used too casually
- keep citations / paper ids with every summary

## Related files

- `templates/paper-reading-log-template.md`
