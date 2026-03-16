# Workflow: Overnight Mini-App Builder

## Purpose

Create a safe lane for the agent to spend off-hours building small prototype apps or utilities that move the user toward an existing goal.

## When to use

- the user explicitly wants surprise prototypes or MVPs
- there is a clear goal context to optimize for
- the environment supports local code generation and file-based review

## Inputs

- current goals / backlog
- time budget for overnight work
- preferred stack or default stack
- safety constraints and approval boundaries

## Outputs

- one prototype concept selection
- implementation artifact in a predictable directory
- short build note with what was built, why, and how to test it

## Procedure

1. Start only after the user explicitly opts in to surprise overnight builds.
2. Select one build candidate that is:
   - aligned to an existing goal
   - small enough for an overnight MVP
   - testable locally
   - low-risk if incomplete
3. Write a short build brief before implementation.
4. Build in a dedicated workspace path such as `projects/overnight/YYYY-MM-DD-slug/`.
5. Prefer local prototypes, internal tools, dashboards, scripts, or draft SaaS MVPs.
6. Leave a concise handoff note with:
   - what it does
   - where the files are
   - how to run/test it
   - what is unfinished
7. Surface the result in the next morning brief or project state update.

## Recommended artifact layout

Inside each overnight build folder, keep the handoff obvious:

- `projects/overnight/YYYY-MM-DD-slug/README.md` or app files
- `projects/overnight/YYYY-MM-DD-slug/BUILD_NOTE.md`
- optional `projects/overnight/YYYY-MM-DD-slug/screenshots/`
- optional `projects/overnight/YYYY-MM-DD-slug/tests/`

Use `templates/task-brief-template.md` for the pre-build brief and `templates/overnight-build-note-template.md` for the handoff note.

## Selection heuristics

Good overnight candidates usually:

- reduce friction on a real recurring task
- turn an existing manual workflow into a local prototype
- produce something the user can inspect in under 10 minutes next morning
- have a clear next step if the prototype lands well

Avoid candidates that mostly generate novelty without changing the user's actual leverage.

## Safety rules

- never deploy publicly without explicit approval
- never buy services, send messages, or publish content automatically
- never modify critical host configuration as part of a surprise build
- prefer local-only artifacts first
- if secrets, billing, or production credentials are needed, stop at scaffold/demo stage

## Verification

- the artifact exists at a predictable path
- the prototype is tied to a real user goal
- a human can inspect and test it the next day
- unfinished work is clearly labeled instead of hidden
- the next morning brief can link to the exact build folder and note

## Risks / gotchas

- surprise is good; wasted effort is not
- small, sharp prototypes beat bloated half-products
- without a clear goal map, surprise builds drift into novelty theater
- if overnight work is not surfaced clearly the next morning, it may as well not have happened

## Related files

- `workflows/goal-driven-autonomous-tasks.md`
- `workflows/autonomous-project-management.md`
- `workflows/multi-agent-handoff-review.md`
- `workflows/morning-brief.md`
- `templates/overnight-build-note-template.md`
- `examples/example-overnight-build-note.md`
