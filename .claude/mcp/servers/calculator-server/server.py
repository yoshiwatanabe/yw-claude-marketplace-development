#!/usr/bin/env python3
"""
Calculator Server - Minimal MCP with multiple tools.

Demonstrates multiple tools in a single MCP server using proper
JSON-RPC 2.0 protocol:
- add, subtract, multiply, divide (with error handling)

Educational Example: Shows how a real MCP server handles multiple tools
and implements proper JSON-RPC 2.0 protocol.
"""

import json
import sys


def handle_initialize(request_id):
    """Handle MCP initialization request."""
    return {
        "jsonrpc": "2.0",
        "id": request_id,
        "result": {
            "protocolVersion": "2024-11-05",
            "capabilities": {},
            "serverInfo": {
                "name": "calculator-server",
                "version": "1.0.0"
            }
        }
    }


def handle_tools_list(request_id):
    """Return available tools."""
    return {
        "jsonrpc": "2.0",
        "id": request_id,
        "result": {
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
    }


def handle_tools_call(request_id, tool_name, arguments):
    """Execute a tool and return result."""
    try:
        a = arguments.get("a")
        b = arguments.get("b")

        if tool_name == "add":
            result = a + b
        elif tool_name == "subtract":
            result = a - b
        elif tool_name == "multiply":
            result = a * b
        elif tool_name == "divide":
            if b == 0:
                return {
                    "jsonrpc": "2.0",
                    "id": request_id,
                    "result": {
                        "content": [
                            {"type": "text", "text": "Error: Division by zero"}
                        ]
                    }
                }
            result = a / b
        else:
            return {
                "jsonrpc": "2.0",
                "id": request_id,
                "error": {
                    "code": -32601,
                    "message": "Tool not found"
                }
            }

        return {
            "jsonrpc": "2.0",
            "id": request_id,
            "result": {
                "content": [
                    {"type": "text", "text": f"Result: {result}"}
                ]
            }
        }

    except Exception as e:
        return {
            "jsonrpc": "2.0",
            "id": request_id,
            "error": {
                "code": -32603,
                "message": f"Calculation error: {str(e)}"
            }
        }


def handle_request(request):
    """
    Handle JSON-RPC 2.0 requests.

    This demonstrates proper MCP protocol handling with multiple tools:
    - Extracts jsonrpc, id, method, params from request
    - Dispatches to appropriate handler
    - Returns JSON-RPC 2.0 formatted response with proper error codes
    """
    request_id = request.get("id")
    method = request.get("method")

    try:
        if method == "initialize":
            return handle_initialize(request_id)

        elif method == "tools/list":
            return handle_tools_list(request_id)

        elif method == "tools/call":
            params = request.get("params", {})
            tool_name = params.get("name")
            arguments = params.get("arguments", {})
            return handle_tools_call(request_id, tool_name, arguments)

        else:
            return {
                "jsonrpc": "2.0",
                "id": request_id,
                "error": {
                    "code": -32601,
                    "message": f"Method not found: {method}"
                }
            }

    except Exception as e:
        return {
            "jsonrpc": "2.0",
            "id": request_id,
            "error": {
                "code": -32603,
                "message": f"Internal error: {str(e)}"
            }
        }


def main():
    """Main server loop - reads JSON-RPC 2.0 requests from stdin."""
    while True:
        try:
            line = sys.stdin.readline()
            if not line:
                break

            request = json.loads(line)
            response = handle_request(request)
            print(json.dumps(response))
            sys.stdout.flush()

        except json.JSONDecodeError:
            error_response = {
                "jsonrpc": "2.0",
                "id": None,
                "error": {
                    "code": -32700,
                    "message": "Parse error"
                }
            }
            print(json.dumps(error_response))
            sys.stdout.flush()

        except KeyboardInterrupt:
            break


if __name__ == "__main__":
    main()
