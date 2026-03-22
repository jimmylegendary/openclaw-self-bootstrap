# WebChat Side Session

## Purpose

Create a fresh WebChat-visible session without killing the current main session.

Use this when:
- the current session is overloaded or noisy
- a human wants a clean branch for a new topic
- you need to preserve the current conversation while opening a second chat lane

## Why this does not need a skill

This workflow can be executed with Gateway operator calls only.
A markdown workflow is enough because the mechanism is stable and explicit:
- create a new session-store entry
- seed it with an assistant bootstrap note
- optionally verify it with a test turn

A helper script is convenient, but not required.

## Canonical key pattern

Use a new WebChat-scoped session key:

```text
agent:<agentId>:webchat:channel:<slug>
```

Example:

```text
agent:main:webchat:channel:jimmy-fresh-session-20260322
```

## Manual procedure

### 1. Create the session entry

```bash
openclaw gateway call sessions.patch --params '{
  "key": "agent:main:webchat:channel:jimmy-fresh-session-20260322",
  "label": "Jimmy Fresh Session"
}'
```

### 2. Seed it with a bootstrap message

```bash
openclaw gateway call chat.inject --params '{
  "sessionKey": "agent:main:webchat:channel:jimmy-fresh-session-20260322",
  "message": "Fresh session created. You can continue chatting here.",
  "label": "Session bootstrap"
}'
```

### 3. Verify it exists

```bash
openclaw gateway call sessions.list --params '{}'
```

Look for:
- the new `key`
- the human-readable `label`
- a new `sessionId`

### 4. Optional: verify it is actually chat-capable

```bash
openclaw gateway call chat.send --params '{
  "sessionKey": "agent:main:webchat:channel:jimmy-fresh-session-20260322",
  "message": "Say only: fresh-session-ok",
  "idempotencyKey": "fresh-session-check-1"
}'

sleep 3

openclaw gateway call chat.history --params '{
  "sessionKey": "agent:main:webchat:channel:jimmy-fresh-session-20260322"
}'
```

## Expected result

The new session appears in WebChat / Control UI session lists as a separate conversation lane.
The current main session remains untouched.

## TUI entry

```bash
openclaw tui --session agent:main:webchat:channel:jimmy-fresh-session-20260322
```

## Operational notes

- `sessions_spawn` is not the reliable path for this on WebChat when channel hooks do not support thread-bound spawning.
- `sessions.patch` + `chat.inject` is the reliable operator path.
- Prefer labels that humans can recognize quickly in the UI.
- Use a slug that is stable, short, and topic-specific.

## Repository policy

Document new session-management workflows here first.
If a portable/export bundle is needed later, generate it from the bootstrap repository instead of maintaining a second source-of-truth repo.
