# Source Notes: awesome-openclaw-skills

## Source
- https://github.com/VoltAgent/awesome-openclaw-skills

## Why this source matters
- large discovery surface for community skills
- useful for finding patterns and install candidates
- should not be trusted blindly

## Key takeaways
- use it as a discovery index, not as an approval signal
- large public skill ecosystems need vetting discipline
- security and scope review must happen before installation

## Patterns pulled from this source
- skill-vetting as a required adoption gate
- multi-agent orchestration as a reusable workflow pattern
- session wrap-up as an end-of-work operating pattern
- active maintenance as a possible future maintenance layer
- continuity / memory-reflection skills as a pattern worth watching, but not yet trusted by default

## Referenced items from our review
- `azhua-skill-vetter`
- `agent-team-orchestration`
- `alex-session-wrap-up`
- `active-maintenance`
- `continuity-framework`
- `ops-hygiene`
- `heartbeats`

## 2026-03-17 environment review
- installed and smoke-tested: `agent-team-orchestration`
- deferred: `session-wrap-up` (VirusTotal flag), `heartbeats` (VirusTotal flag)
- deferred: `continuity-framework` (prototype quality, mismatched paths)
- deferred: `ops-hygiene` (hardcoded dependencies on extra local services and secrets)

## Decision rule reinforced by this review
- prefer doc-only or local-first skills with clear scope and no hidden service assumptions
- do not treat a polished README as evidence of safe fit on this machine
- if a skill assumes extra daemons, local APIs, or secret files, document it as environment-specific until proven here

## How to use this source
1. find candidate skills by use case
2. record them in `skills/registry.md`
3. run the skill vetting workflow
4. only then install or reject
