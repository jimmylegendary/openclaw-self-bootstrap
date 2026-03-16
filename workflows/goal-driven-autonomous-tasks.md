# Workflow: Goal-Driven Autonomous Tasks

## Purpose

Turn a user's long-horizon goals into a controlled daily execution loop that the agent can plan, schedule, and complete with minimal micromanagement.

## When to use

- the user has many goals but weak day-to-day execution bandwidth
- the user wants proactive task generation, not only reactive help
- the system can already write files, run local work, and keep project state

## Inputs

- goal dump from the user
- constraints, priorities, and no-go zones
- available tools / skills
- optional schedule windows for morning planning and overnight work

## Outputs

- compact goals file
- daily autonomous task shortlist
- execution log of completed work
- optional overnight mini-app lane

## Procedure

1. Ask the user for a plain-language goal dump.
2. Distill it into a compact goals/backlog file rather than leaving it only in chat.
3. Separate the system into two files:
   - one small control file for active goals and open backlog
   - one append-only completion log for finished tasks
4. Generate only a small daily task set (usually 3-5 items).
5. Prefer tasks that are:
   - concretely executable on the current machine
   - aligned to current goals
   - useful without needing constant approvals
   - small enough to verify
6. Track task state in project files, not only in transient chat.
7. Use subagents for multi-step work, but require them to append results to the log instead of rewriting the control file.
8. Review outcomes and prune low-value task patterns over time.

## Suggested file split

Keep the planning/control surface small.

- `AUTONOMOUS.md` or `ops/autonomous-goals.md`
  - goals
  - active backlog
  - active task shortlist
- `memory/tasks-log.md`
  - append-only completion log
  - subagents append only; never rewrite history

This avoids edit collisions and keeps recurring context cheap to load.

## Verification

- the daily task list is short, concrete, and clearly goal-linked
- completed work is visible from files alone
- subagent writes do not race on the same control file
- the loop can resume cleanly after a session reset

## Risks / gotchas

- do not give the agent open-ended freedom without clear user priorities
- do not let the control file grow into a giant archive
- do not schedule automation before the task-selection quality proves useful manually
- avoid tasks that need external posting, payments, destructive changes, or risky installs without explicit approval

## Related files

- `workflows/autonomous-project-management.md`
- `workflows/project-state-tracking.md`
- `workflows/morning-brief.md`
- `templates/task-brief-template.md`
- `sources/awesome-openclaw-usecases.md`
