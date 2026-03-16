# Workflow: Multi-Agent Specialized Team

## Purpose

Run a small team of specialized agents with shared project context and clear role boundaries.

## When to use

- ongoing work that spans strategy, research, implementation, or review
- situations where one generic agent becomes a bottleneck

## Inputs

- team roles
- routing rules
- shared files for goals, decisions, and status

## Outputs

- role-based subagent structure
- shared team context files
- clearer division of labor

## Procedure

1. Start with 2 agents, not 4.
2. Define a lead/orchestrator role and one specialist role.
3. Create shared files for goals, decisions, and project status.
4. Give each role a narrow responsibility.
5. Add scheduled tasks only after the team proves useful manually.
6. Expand the team only when a real bottleneck appears.

## Verification

- each role has a clear job
- handoffs update shared state
- the team reduces context switching instead of increasing it

## Risks / gotchas

- too many agents too early creates coordination overhead
- shared context must stay clean or the team drifts

## Related files

- `workflows/multi-agent-handoff-review.md`
- `templates/team-routing-template.md`
