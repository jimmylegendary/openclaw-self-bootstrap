# Workflow: Morning Brief

## Purpose

Give the user a concise daily orientation with priorities, risks, and proactive suggestions.

## When to use

- daily startup routine
- before scheduling any morning summary automation

## Inputs

- active work snapshot
- relevant reminders or risks
- optional external sources such as calendar, tasks, feeds, or email

## Outputs

- one concise morning briefing

## Procedure

1. Start in manual mode first.
2. Use `templates/morning-brief-template.md`.
3. Include only useful signals; avoid generic filler.
4. Tune sections for a few runs.
5. Only after manual success, schedule delivery.

## Verification

- useful enough that the user would actually want to read it
- focused on current priorities and likely misses
- no irrelevant news padding

## Risks / gotchas

- low-quality briefs become noise fast
- do not schedule before the content proves useful

## Related files

- `templates/morning-brief-template.md`
- `examples/example-morning-brief.md`
