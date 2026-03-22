#!/usr/bin/env python3
import json
import subprocess
import sys
from typing import Any, Dict

SERVER_CMD = [sys.executable, "mcp-test-server.py"]


def write_message(proc: subprocess.Popen, obj: Dict[str, Any]) -> None:
    body = json.dumps(obj).encode("utf-8")
    proc.stdin.write(f"Content-Length: {len(body)}\r\n\r\n".encode("ascii"))
    proc.stdin.write(body)
    proc.stdin.flush()


def read_message(proc: subprocess.Popen) -> Dict[str, Any]:
    headers = {}
    while True:
        line = proc.stdout.readline()
        if not line:
            raise RuntimeError("server closed stdout")
        if line in (b"\r\n", b"\n"):
            break
        key, value = line.decode("utf-8").split(":", 1)
        headers[key.strip().lower()] = value.strip()
    length = int(headers["content-length"])
    body = proc.stdout.read(length)
    return json.loads(body.decode("utf-8"))


def rpc(proc: subprocess.Popen, msg_id: int, method: str, params: Dict[str, Any] | None = None) -> Dict[str, Any]:
    payload = {"jsonrpc": "2.0", "id": msg_id, "method": method}
    if params is not None:
        payload["params"] = params
    write_message(proc, payload)
    return read_message(proc)


if __name__ == "__main__":
    proc = subprocess.Popen(
        SERVER_CMD,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd="/home/jimmy/.openclaw/workspace",
    )
    assert proc.stdin and proc.stdout

    try:
        init = rpc(proc, 1, "initialize", {"protocolVersion": "2024-11-05", "capabilities": {}, "clientInfo": {"name": "local-test", "version": "0.1"}})
        write_message(proc, {"jsonrpc": "2.0", "method": "notifications/initialized", "params": {}})
        tools = rpc(proc, 2, "tools/list", {})
        ping = rpc(proc, 3, "tools/call", {"name": "ping", "arguments": {}})
        echo = rpc(proc, 4, "tools/call", {"name": "echo", "arguments": {"text": "hello mcp"}})

        print(json.dumps({
            "initialize": init,
            "tools": tools,
            "ping": ping,
            "echo": echo,
        }, indent=2, ensure_ascii=False))
    finally:
        proc.kill()
        proc.wait(timeout=3)
