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
- optional overnight output that needs surfacing

## Outputs

- one concise morning briefing

## Procedure

1. Start in manual mode first.
2. Use `templates/morning-brief-template.md`.
3. Pull current priorities from `ops/autonomous-goals.md` or project state.
4. If overnight work happened, include a reviewable pointer to the exact artifact path.
5. Include only useful signals; avoid generic filler.
6. Tune sections for a few runs.
7. Only after manual success, schedule delivery.

## Verification

- useful enough that the user would actually want to read it
- focused on current priorities and likely misses
- overnight output is surfaced with exact paths when relevant
- no irrelevant news padding

## Risks / gotchas

- low-quality briefs become noise fast
- do not schedule before the content proves useful
- if the brief never points to concrete files, it will drift into vague status theater

## Related files

- `templates/morning-brief-template.md`
- `examples/example-morning-brief.md`
- `workflows/goal-driven-autonomous-tasks.md`
- `workflows/overnight-mini-app-builder.md`
