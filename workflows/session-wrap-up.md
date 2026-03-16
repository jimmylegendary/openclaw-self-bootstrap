# Workflow: Session Wrap-Up

## Purpose

End meaningful work cleanly so context is preserved and future work starts from a known state.

## When to use

- end of a meaningful work block
- before long idle time
- when explicitly asked to wrap up

## Inputs

- files changed
- decisions made
- blockers
- next actions

## Outputs

- short wrap-up summary
- updated memory and/or project-state files
- clean commit if appropriate

## Procedure

1. Summarize what changed.
2. Record decisions, blockers, and next actions.
3. Update daily memory and project state where relevant.
4. Check git status.
5. Commit intentional changes with a useful message.
6. Do not auto-push unless explicitly asked.

## Verification

- the next session knows where to resume
- important context is in files, not only chat
- commit message reflects actual work

## Risks / gotchas

- avoid fake certainty
- avoid noisy, scattered summaries

## Related files

- `templates/session-wrap-up-template.md`
