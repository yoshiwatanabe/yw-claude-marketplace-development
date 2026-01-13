#!/usr/bin/env python3
"""
Calculator Server - MCP server with multiple tools.

Demonstrates multiple tools in a single MCP server:
- add, subtract, multiply, divide
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
                    "name": "add",
                    "description": "Add two numbers",
                    "inputSchema": {
                        "type": "object",
                        "properties": {
                            "a": {"type": "number", "description": "First number"},
                            "b": {"type": "number", "description": "Second number"}
                        },
                        "required": ["a", "b"]
                    }
                },
                {
                    "name": "subtract",
                    "description": "Subtract two numbers",
                    "inputSchema": {
                        "type": "object",
                        "properties": {
                            "a": {"type": "number", "description": "First number"},
                            "b": {"type": "number", "description": "Second number"}
                        },
                        "required": ["a", "b"]
                    }
                },
                {
                    "name": "multiply",
                    "description": "Multiply two numbers",
                    "inputSchema": {
                        "type": "object",
                        "properties": {
                            "a": {"type": "number", "description": "First number"},
                            "b": {"type": "number", "description": "Second number"}
                        },
                        "required": ["a", "b"]
                    }
                },
                {
                    "name": "divide",
                    "description": "Divide two numbers",
                    "inputSchema": {
                        "type": "object",
                        "properties": {
                            "a": {"type": "number", "description": "Numerator"},
                            "b": {"type": "number", "description": "Denominator"}
                        },
                        "required": ["a", "b"]
                    }
                }
            ]
        }

    elif request.get("method") == "tools/call":
        tool_name = request.get("params", {}).get("name")
        arguments = request.get("params", {}).get("arguments", {})

        a = arguments.get("a")
        b = arguments.get("b")

        try:
            if tool_name == "add":
                result = a + b
            elif tool_name == "subtract":
                result = a - b
            elif tool_name == "multiply":
                result = a * b
            elif tool_name == "divide":
                if b == 0:
                    return {
                        "content": [
                            {"type": "text", "text": "Error: Division by zero"}
                        ]
                    }
                result = a / b
            else:
                return {"error": "Unknown tool"}

            return {
                "content": [
                    {"type": "text", "text": f"Result: {result}"}
                ]
            }

        except Exception as e:
            return {
                "content": [
                    {"type": "text", "text": f"Error: {str(e)}"}
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
