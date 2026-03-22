# openclaw-self-bootstrap

A public, agent-readable bootstrap repo for turning a fresh OpenClaw install into a safer, more structured operating system.

This repo is optimized for OpenClaw agents to read and apply, not just for humans to browse.

## What it contains

- operating workflows that are not part of OpenClaw defaults
- safe skill adoption rules
- project-state and wrap-up patterns
- a pre-build idea validation gate
- second-brain and personal knowledge-base patterns
- autonomous project-management and meeting-notes workflows
- goal-driven autonomous task planning and an overnight mini-app builder lane
- specialized-team, arXiv reading, and LaTeX writing extensions
- a first-pass morning-brief workflow
- a reusable multi-agent handoff/review pattern
- a WebChat side-session workflow for opening a fresh session without killing the current one
- source notes from community awesome lists
- a small vetted record of which third-party skills were actually reviewed, installed, tested, or deferred on a real machine

## Intended use

1. Install OpenClaw.
2. Clone this repo into a workspace.
3. Have the agent read `AGENT_START_HERE.md`.
4. Apply workflows in `APPLY_ORDER.md`.
5. Use `skills/registry.md` and `sources/` before adding new skills.

## Daily loop added by this repo

The autonomy-oriented workflows are meant to form one file-backed loop:

1. plan from `ops/autonomous-goals.md`
2. execute a short daily shortlist
3. optionally build one overnight artifact in `projects/overnight/YYYY-MM-DD-slug/`
4. surface outcomes in the next morning brief or project-state update
5. append completed work to `memory/tasks-log.md`

Templates and examples for this loop live in `templates/` and `examples/`.

## Design goal

Make it easy for an OpenClaw agent to bootstrap itself safely and consistently.

## Repository position

Treat this repository as the canonical source-of-truth for bootstrap and operating workflows.
If a portable bundle is needed later, generate or curate it from here rather than maintaining a second competing repo of overlapping guidance.
