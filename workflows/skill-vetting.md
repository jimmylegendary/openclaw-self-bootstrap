# Workflow: Skill Vetting

## Purpose

Prevent unsafe or low-fit third-party skills from being installed casually.

## When to use

- before installing any non-bundled skill
- before recommending a GitHub-hosted skill
- before adopting a workflow that requires new credentials or external APIs

## Inputs

- candidate skill URL
- claimed use case
- existing built-in alternatives

## Outputs

- completed vetting record
- risk level
- verdict: install | caution | reject

## Procedure

1. Copy `templates/skill-vetting-template.md`.
2. Record purpose, source, maintainer, and trust signals.
3. Evaluate file, network, credential, and command scope.
4. Check red flags.
5. Decide risk rating and rollout scope.
6. Only then install or reject.

## Verification

- the skill has a clear purpose
- scope matches purpose
- no major unexplained red flags
- safer alternatives were considered

## Risks / gotchas

- skills can look useful but request broad permissions
- popularity is not the same as safety
- avoid storing credentials directly in skill code or workspace docs

## Related files

- `templates/skill-vetting-template.md`
- `skills/registry.md`
