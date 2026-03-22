# OpenClaw Portable Kit

> Canonical home: `openclaw-self-bootstrap`
> This directory is the portable/export layer embedded inside the canonical bootstrap repository.
> New workflows and durable operating knowledge should be added to the root repository first, then exported or curated here only when portability matters.

다른 OpenClaw 환경에 옮겨 설치할 수 있게 정리한 포터블 번들이다.

포함 내용:
- `templates/` — 작업 기본 성격/운영용 MD 템플릿
- `skills/` — 현재 시스템에서 검증/사용 중인 커스텀 skill 묶음
- `mcp-examples/` — 로컬 MCP 테스트 서버 예제
- `scripts/install.sh` — 대상 OpenClaw workspace에 설치하는 스크립트
- `manifest.json` — 포함 항목 메타데이터

## 의도
이 번들은 **다른 OpenClaw 인스턴스에 복제 가능한 운영 레이어**를 옮기기 위한 것이다.

즉,
- persona / workspace 운영 규칙용 MD
- 재사용 가능한 로컬 skill
- MCP 테스트 예제
를 한 번에 옮길 수 있다.

## 포함되지 않는 것
안전하게 제외한 것:
- `MEMORY.md`, `memory/` 같은 개인 기억/로그
- 토큰, API 키, credential 파일
- quarantine 스킬
- 호스트 고유 비밀값

## 설치
대상 머신의 OpenClaw workspace에서:

```bash
bash scripts/install.sh /path/to/target-workspace
```

예:

```bash
bash scripts/install.sh ~/.openclaw/workspace
```

기본 동작:
- `templates/`의 MD 파일을 대상 루트에 복사
- `skills/`의 skill 디렉토리를 대상 `skills/` 아래에 복사
- `mcp-examples/`를 대상 루트의 `mcp-examples/`로 복사
- 이미 같은 파일/디렉토리가 있으면 `.bak.YYYYMMDDHHMMSS` 백업 후 교체

## 추천 후속 작업
설치 후 대상 환경에서 확인:

```bash
openclaw status
```

필요하면 skill 바이너리 유무도 체크:

```bash
which mcporter
which claude
which gh
```

## MCP 예제 테스트
설치 후:

```bash
python3 mcp-examples/test_mcp_server.py
```

## 포함한 skill 목록
- agent-browser
- agent-team-orchestration
- find-skills
- mcporter
- notion
- proactive-agent
- self-improving-agent
- session-logs
- skill-vetter
- summarize
- tmux
