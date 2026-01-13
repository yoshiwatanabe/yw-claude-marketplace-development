#!/usr/bin/env python3
"""
Echo Server - Minimal MCP (Model Context Protocol) implementation.

Demonstrates a basic MCP server that echoes back input using proper
JSON-RPC 2.0 protocol. This shows how MCP servers actually communicate
with clients using the standard protocol.

Educational Example: This implementation shows the minimal JSON-RPC 2.0
protocol handling needed for a real MCP server.
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
                "name": "echo-server",
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
    }


def handle_tools_call(request_id, tool_name, arguments):
    """Execute a tool and return result."""
    if tool_name == "echo":
        message = arguments.get("message", "")
        return {
            "jsonrpc": "2.0",
            "id": request_id,
            "result": {
                "content": [
                    {
                        "type": "text",
                        "text": f"Echo: {message}"
                    }
                ]
            }
        }
    else:
        return {
            "jsonrpc": "2.0",
            "id": request_id,
            "error": {
                "code": -32601,
                "message": "Tool not found"
            }
        }


def handle_request(request):
    """
    Handle JSON-RPC 2.0 requests.

    This demonstrates proper MCP protocol handling:
    - Extracts jsonrpc, id, method, params from request
    - Dispatches to appropriate handler
    - Returns JSON-RPC 2.0 formatted response
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
            # Unknown method
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

        except json.JSONDecodeError as e:
            # Invalid JSON - send parse error response
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
