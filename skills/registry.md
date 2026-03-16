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

### Workflow: Pre-build idea validator
- Type: workflow
- Status: applied
- Risk: low
- Why: prevents blind building before checking competitive reality
- Files:
  - `workflows/pre-build-idea-validator.md`
  - `templates/idea-validator-template.md`

### Workflow: Second brain
- Type: workflow
- Status: applied
- Risk: low
- Why: creates low-friction memory capture
- Files:
  - `workflows/second-brain.md`

### Workflow: Personal knowledge base
- Type: workflow
- Status: applied
- Risk: low
- Why: separates external research corpus from personal memory
- Files:
  - `workflows/personal-knowledge-base.md`

### Workflow: Autonomous project management
- Type: workflow
- Status: applied-lean
- Risk: medium
- Why: allows shared state coordination for bigger projects without full micromanagement
- Files:
  - `workflows/autonomous-project-management.md`
  - `templates/state-yaml-template.yaml`

### Workflow: Meeting notes & action items
- Type: workflow
- Status: applied-local-first
- Risk: medium
- Why: turns transcripts into decisions and action items before external task sync
- Files:
  - `workflows/meeting-notes-action-items.md`
  - `templates/meeting-notes-template.md`

### Workflow: Multi-agent specialized team
- Type: workflow
- Status: applied-staged
- Risk: medium
- Why: role-based specialization can reduce context switching if introduced gradually
- Files:
  - `workflows/multi-agent-specialized-team.md`
  - `templates/team-routing-template.md`

### Workflow: arXiv paper reader
- Type: workflow
- Status: applied-pattern
- Risk: medium
- Why: gives a structured research-reading loop for papers
- Files:
  - `workflows/arxiv-paper-reader.md`
  - `templates/paper-reading-log-template.md`

### Workflow: LaTeX paper writing
- Type: workflow
- Status: applied-pattern
- Risk: medium
- Why: captures a reproducible writing/compile loop for technical papers
- Files:
  - `workflows/latex-paper-writing.md`
  - `templates/latex-paper-template.md`

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
