# Skill Vetting Template

- Skill name:
- Source URL:
- Author:
- Claimed purpose:
- Why we want it now:
- Existing built-in alternative:

## Trust signals
- Repo / registry:
- Popularity:
- Last updated:
- Official OpenClaw skills repo?: yes/no

## Required access
### Filesystem
- Reads:
- Writes:
- Outside workspace needed?:

### Network
- Domains / APIs:
- Webhooks / exfil risk:

### Credentials
- API keys / tokens / OAuth:
- Isolation plan:

### Commands
- Shell commands:
- Package installs:
- Elevated privileges:

## Red flags
- [ ] Reads private identity files without clear reason
- [ ] Broad dotfile / credential access
- [ ] Sends data to unknown servers
- [ ] Obfuscated or encoded logic
- [ ] Uses eval/exec/dynamic remote code loading
- [ ] Writes outside intended scope
- [ ] Requests elevated privileges
- [ ] Hidden dependencies
- [ ] Suspicious domains or raw IPs
- [ ] Permissions exceed stated purpose

## Risk
- Rating:
- Verdict:
- Safe rollout scope:
- Human approval needed?:
- Notes:
