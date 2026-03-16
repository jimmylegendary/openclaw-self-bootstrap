# Workflow: Autonomous Project Management

## Purpose

Coordinate multi-step work through shared project state so subagents can make progress without constant main-session micromanagement.

## When to use

- projects with multiple parallel tasks
- work that will span multiple sessions or agents
- cases where a lightweight PM layer helps

## Inputs

- project name
- task list
- owners / labels
- blockers and dependencies

## Outputs

- project state file
- delegated tasks with owners and status
- resumable record of progress

## Procedure

1. Create a project state file for the project.
2. Break work into named tasks.
3. Record status, owner, notes, and dependencies.
4. Delegate tasks to subagents with exact scope.
5. Update project state on meaningful changes.
6. Keep the main session focused on direction, not every sub-step.

## Verification

- project status is visible from files alone
- delegated work has explicit ownership
- blockers and next actions are current

## Risks / gotchas

- do not overbuild the PM layer for tiny projects
- state files only help if they stay current

## Related files

- `workflows/project-state-tracking.md`
- `workflows/multi-agent-handoff-review.md`
- `templates/state-yaml-template.yaml`
