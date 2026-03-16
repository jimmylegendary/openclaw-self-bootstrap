# Workflow: Project State Tracking

## Purpose

Keep a shared, current source of truth for active work so future sessions can resume without reconstructing everything from chat.

## When to use

- any ongoing project
- work with blockers, decisions, or next actions
- work likely to continue across sessions

## Inputs

- project name
- current status
- latest progress, decisions, blockers, and next actions

## Outputs

- updated project-state document

## Procedure

1. Create or update a project section using `templates/project-state-template.md`.
2. Record status, current focus, and last updated date.
3. Add recent progress when meaningful work happens.
4. Add decisions when direction changes.
5. Add blockers when work is stalled.
6. Keep next actions concrete.

## Verification

- another session could resume the work from the file alone
- blockers and next actions are explicit
- current status is not stale

## Risks / gotchas

- do not dump daily chatter here
- keep this for shared current state, not raw logs

## Related files

- `templates/project-state-template.md`
- `examples/example-project-state.md`
