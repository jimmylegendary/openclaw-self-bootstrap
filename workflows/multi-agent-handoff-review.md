# Workflow: Multi-Agent Handoff / Review

## Purpose

Make delegated work resumable, reviewable, and less dependent on hidden chat context.

## When to use

- non-trivial delegated work
- tasks with multiple artifacts or steps
- work that benefits from a second pass

## Inputs

- task id
- output path
- acceptance criteria
- builder and reviewer responsibilities

## Outputs

- task brief
- builder artifact with handoff
- reviewer result
- final summary

## Procedure

1. Create a task folder.
2. Write a task brief using `templates/task-brief-template.md`.
3. Assign a builder and define exact output paths.
4. Require a structured builder handoff.
5. Run a reviewer pass for clarity, risks, and completeness.
6. Save the final summary in the same task folder.

## Verification

- next agent can continue without guessing
- output paths are explicit
- review result is recorded

## Risks / gotchas

- this pattern is overkill for tiny tasks
- vague handoffs erase most of the value
- predictable paths matter more than clever prompts

## Related files

- `templates/task-brief-template.md`
- `templates/builder-handoff-template.md`
- `templates/reviewer-output-template.md`
- `examples/handoff-test/`
