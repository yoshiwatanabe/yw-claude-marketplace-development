#!/usr/bin/env python3
"""
Weather Server - Minimal MCP with external API integration.

Demonstrates an MCP server that integrates with an external API (Open-Meteo)
using proper JSON-RPC 2.0 protocol. Provides current weather and forecast
data for any location.

Educational Example: Shows how MCP servers handle real API integration
with proper protocol implementation and error handling.
"""

import json
import sys
import requests


def get_weather(latitude, longitude):
    """Fetch weather data from Open-Meteo API."""
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,wind_speed_10m,weather_code",
        "hourly": "temperature_2m,relative_humidity_2m,wind_speed_10m",
        "timezone": "auto"
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}


def format_weather(data):
    """Format weather data for display."""
    if "error" in data:
        return f"Error fetching weather: {data['error']}"

    current = data.get("current", {})
    location = data.get("latitude", 0), data.get("longitude", 0)

    result = f"""
Current Weather at {location}:
- Temperature: {current.get('temperature_2m', 'N/A')}°C
- Wind Speed: {current.get('wind_speed_10m', 'N/A')} km/h
- Timezone: {data.get('timezone', 'N/A')}
"""

    hourly = data.get("hourly", {})
    if hourly.get("time"):
        times = hourly["time"][:3]  # First 3 hours
        temps = hourly.get("temperature_2m", [])[:3]
        result += "\nNext 3 hours forecast:\n"
        for i, time in enumerate(times):
            result += f"  {time}: {temps[i] if i < len(temps) else 'N/A'}°C\n"

    return result


def handle_initialize(request_id):
    """Handle MCP initialization request."""
    return {
        "jsonrpc": "2.0",
        "id": request_id,
        "result": {
            "protocolVersion": "2024-11-05",
            "capabilities": {},
            "serverInfo": {
                "name": "weather-server",
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
                    "name": "get_weather",
                    "description": "Get current weather and hourly forecast for a location",
                    "inputSchema": {
                        "type": "object",
                        "properties": {
                            "latitude": {
                                "type": "number",
                                "description": "Latitude of the location"
                            },
                            "longitude": {
                                "type": "number",
                                "description": "Longitude of the location"
                            }
                        },
                        "required": ["latitude", "longitude"]
                    }
                }
            ]
        }
    }


def handle_tools_call(request_id, tool_name, arguments):
    """Execute a tool and return result."""
    if tool_name == "get_weather":
        latitude = arguments.get("latitude")
        longitude = arguments.get("longitude")

        if latitude is None or longitude is None:
            return {
                "jsonrpc": "2.0",
                "id": request_id,
                "error": {
                    "code": -32602,
                    "message": "Missing required parameters: latitude and longitude"
                }
            }

        try:
            data = get_weather(latitude, longitude)
            formatted = format_weather(data)

            return {
                "jsonrpc": "2.0",
                "id": request_id,
                "result": {
                    "content": [
                        {"type": "text", "text": formatted}
                    ]
                }
            }
        except Exception as e:
            return {
                "jsonrpc": "2.0",
                "id": request_id,
                "error": {
                    "code": -32603,
                    "message": f"API error: {str(e)}"
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

    This demonstrates proper MCP protocol handling with external API calls:
    - Extracts jsonrpc, id, method, params from request
    - Dispatches to appropriate handler
    - Returns JSON-RPC 2.0 formatted response with proper error codes
    - Shows error handling for API integration
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
