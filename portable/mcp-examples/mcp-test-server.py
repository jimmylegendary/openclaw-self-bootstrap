#!/usr/bin/env python3
import json
import sys
from typing import Any, Dict


def write_message(obj: Dict[str, Any]) -> None:
    body = json.dumps(obj, ensure_ascii=False).encode("utf-8")
    sys.stdout.buffer.write(f"Content-Length: {len(body)}\r\n\r\n".encode("ascii"))
    sys.stdout.buffer.write(body)
    sys.stdout.buffer.flush()


def read_message() -> Dict[str, Any] | None:
    headers = {}
    while True:
        line = sys.stdin.buffer.readline()
        if not line:
            return None
        if line in (b"\r\n", b"\n", b""):
            break
        key, value = line.decode("utf-8").split(":", 1)
        headers[key.strip().lower()] = value.strip()
    length = int(headers.get("content-length", "0"))
    if length <= 0:
        return None
    body = sys.stdin.buffer.read(length)
    if not body:
        return None
    return json.loads(body.decode("utf-8"))


def handle_request(msg: Dict[str, Any]) -> None:
    method = msg.get("method")
    msg_id = msg.get("id")
    params = msg.get("params", {})

    if method == "initialize":
        write_message({
            "jsonrpc": "2.0",
            "id": msg_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "openclaw-test-mcp", "version": "0.1.0"},
            },
        })
        return

    if method == "notifications/initialized":
        return

    if method == "tools/list":
        write_message({
            "jsonrpc": "2.0",
            "id": msg_id,
            "result": {
                "tools": [
                    {
                        "name": "ping",
                        "description": "Return pong with a timestamp-free fixed response.",
                        "inputSchema": {
                            "type": "object",
                            "properties": {},
                            "additionalProperties": False,
                        },
                    },
                    {
                        "name": "echo",
                        "description": "Echo back the provided text.",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "text": {"type": "string"}
                            },
                            "required": ["text"],
                            "additionalProperties": False,
                        },
                    },
                ]
            },
        })
        return

    if method == "tools/call":
        name = params.get("name")
        arguments = params.get("arguments", {}) or {}
        if name == "ping":
            result_text = "pong"
        elif name == "echo":
            result_text = f"echo: {arguments.get('text', '')}"
        else:
            write_message({
                "jsonrpc": "2.0",
                "id": msg_id,
                "error": {"code": -32601, "message": f"Unknown tool: {name}"},
            })
            return

        write_message({
            "jsonrpc": "2.0",
            "id": msg_id,
            "result": {
                "content": [
                    {"type": "text", "text": result_text}
                ]
            },
        })
        return

    if msg_id is not None:
        write_message({
            "jsonrpc": "2.0",
            "id": msg_id,
            "error": {"code": -32601, "message": f"Unsupported method: {method}"},
        })


if __name__ == "__main__":
    while True:
        message = read_message()
        if message is None:
            break
        handle_request(message)
