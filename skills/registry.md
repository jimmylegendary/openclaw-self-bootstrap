# Skill / Workflow Registry

This file tracks additions that are not part of OpenClaw defaults.

## Applied now

### Workflow: Skill vetting
- Type: workflow
- Status: applied
- Risk: low
- Why: required gate before third-party skill adoption
- Files:
  - `workflows/skill-vetting.md`
  - `templates/skill-vetting-template.md`

### Workflow: Project state tracking
- Type: workflow
- Status: applied
- Risk: low
- Why: preserves shared current state across sessions
- Files:
  - `workflows/project-state-tracking.md`
  - `templates/project-state-template.md`

### Workflow: Session wrap-up
- Type: workflow
- Status: applied
- Risk: low
- Why: clean session closure and resumability
- Files:
  - `workflows/session-wrap-up.md`
  - `templates/session-wrap-up-template.md`

### Workflow: Morning brief
- Type: workflow
- Status: manual-draft-only
- Risk: low
- Why: useful daily orientation once tuned manually
- Files:
  - `workflows/morning-brief.md`
  - `templates/morning-brief-template.md`

### Workflow: Multi-agent handoff / review
- Type: workflow
- Status: applied-and-tested
- Risk: low
- Why: improves delegation quality and reviewability
- Files:
  - `workflows/multi-agent-handoff-review.md`
  - `templates/task-brief-template.md`
  - `templates/builder-handoff-template.md`
  - `templates/reviewer-output-template.md`
  - `examples/handoff-test/`

## Candidate patterns to evaluate later

### n8n workflow orchestration
- Type: architecture pattern
- Status: candidate
- Why: isolate credentials and move deterministic API actions out of the model loop
- Risk: medium

### Semantic memory search upgrade
- Type: architecture pattern
- Status: candidate
- Why: useful once markdown memory grows beyond built-in retrieval comfort
- Risk: medium

### Active maintenance / memory metabolism
- Type: maintenance pattern
- Status: candidate
- Why: periodic cleanup and memory distillation may be helpful later
- Risk: medium

## Rule

Do not treat a candidate as installed just because it appears in this registry.
