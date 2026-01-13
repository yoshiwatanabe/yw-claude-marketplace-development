#!/usr/bin/env python3
"""
Weather Server - MCP server wrapping the Open-Meteo API.

Demonstrates an MCP server that integrates with an external API.
Provides current weather and forecast data for any location.
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


def process_request(request):
    """Process incoming MCP requests."""
    if request.get("method") == "tools/list":
        return {
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

    elif request.get("method") == "tools/call":
        tool_name = request.get("params", {}).get("name")
        arguments = request.get("params", {}).get("arguments", {})

        if tool_name == "get_weather":
            latitude = arguments.get("latitude")
            longitude = arguments.get("longitude")

            if latitude is None or longitude is None:
                return {
                    "content": [
                        {"type": "text", "text": "Error: latitude and longitude required"}
                    ]
                }

            data = get_weather(latitude, longitude)
            formatted = format_weather(data)

            return {
                "content": [
                    {"type": "text", "text": formatted}
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
