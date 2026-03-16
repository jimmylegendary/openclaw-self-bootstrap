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

## Recommended daily loop

1. Morning or session-start planning
   - review `ops/autonomous-goals.md`
   - pick a small daily shortlist
   - surface the shortlist in the morning brief or active project state
2. Daytime execution
   - complete 1-3 concrete tasks
   - write outcomes to the task log as work finishes
3. Overnight lane
   - optionally pick one build candidate from the same goals file
   - write a short build brief before implementation
   - keep overnight work isolated to a predictable artifact path
4. Next-morning surfacing
   - summarize completed work, carry-forwards, and overnight output
   - prune stale shortlist items before generating the next day

This keeps planning, execution, and surprise building inside one visible loop instead of three disconnected habits.

## Suggested file split

Keep the planning/control surface small.

- `ops/autonomous-goals.md`
  - goals
  - active backlog
  - active task shortlist
  - overnight candidates
- `memory/tasks-log.md`
  - append-only completion log
  - subagents append only; never rewrite history
- `projects/overnight/YYYY-MM-DD-slug/`
  - optional overnight build workspace
  - include a short `BUILD_NOTE.md` handoff file

This avoids edit collisions and keeps recurring context cheap to load.

## Path conventions

Use stable, boring paths so future sessions can find work without guessing.

- `ops/autonomous-goals.md`
  - single control file for active goals and task selection
- `memory/tasks-log.md`
  - append-only history of completed tasks and notable outcomes
- `projects/overnight/YYYY-MM-DD-slug/`
  - one folder per overnight prototype
- `projects/overnight/YYYY-MM-DD-slug/BUILD_NOTE.md`
  - what was built, why, how to test, what is unfinished

If a repo or project already has its own conventions, mirror this split inside that project rather than inventing a second parallel system.

## Verification

- the daily task list is short, concrete, and clearly goal-linked
- completed work is visible from files alone
- subagent writes do not race on the same control file
- the loop can resume cleanly after a session reset
- next-morning surfacing can point to exact files, not vague memory

## Risks / gotchas

- do not give the agent open-ended freedom without clear user priorities
- do not let the control file grow into a giant archive
- do not schedule automation before the task-selection quality proves useful manually
- avoid tasks that need external posting, payments, destructive changes, or risky installs without explicit approval

## Related files

- `workflows/autonomous-project-management.md`
- `workflows/project-state-tracking.md`
- `workflows/morning-brief.md`
- `templates/autonomous-goals-template.md`
- `templates/task-brief-template.md`
- `templates/overnight-build-note-template.md`
- `sources/awesome-openclaw-usecases.md`
