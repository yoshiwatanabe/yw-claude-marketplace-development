#!/usr/bin/env python3
"""
Echo Server - The simplest possible MCP server.

Demonstrates a basic MCP server that echoes back input.
This is a minimal example with a single tool.
"""

import json
import sys


def process_request(request):
    """Process incoming MCP requests."""
    if request.get("method") == "tools/list":
        # Return available tools
        return {
            "tools": [
                {
                    "name": "echo",
                    "description": "Echoes back the input text",
                    "inputSchema": {
                        "type": "object",
                        "properties": {
                            "message": {
                                "type": "string",
                                "description": "Text to echo"
                            }
                        },
                        "required": ["message"]
                    }
                }
            ]
        }

    elif request.get("method") == "tools/call":
        tool_name = request.get("params", {}).get("name")
        arguments = request.get("params", {}).get("arguments", {})

        if tool_name == "echo":
            message = arguments.get("message", "")
            return {
                "content": [
                    {
                        "type": "text",
                        "text": f"Echo: {message}"
                    }
                ]
            }

    return {"error": "Unknown request"}


def main():
    """Main server loop."""
    while True:
        try:
            line = sys.stdin.readline()
            if not line:
                break

            request = json.loads(line)
            response = process_request(request)
            print(json.dumps(response))
            sys.stdout.flush()

        except (json.JSONDecodeError, KeyboardInterrupt):
            break


if __name__ == "__main__":
    main()
