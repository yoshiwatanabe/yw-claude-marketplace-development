# MCP Servers Demo

This directory contains three MCP (Model Context Protocol) servers demonstrating different patterns of tool integration.

## Servers

### 1. Echo Server
**Pattern:** Minimal MCP server with a single tool

- **Tool:** `echo` - Echoes back input text
- **Dependencies:** None (standard library only)
- **Use case:** Learning the basics of MCP server structure
- **Test:** Ask Claude "Echo hello world"

### 2. Calculator Server
**Pattern:** Multiple tools in one server

- **Tools:**
  - `add` - Add two numbers
  - `subtract` - Subtract two numbers
  - `multiply` - Multiply two numbers
  - `divide` - Divide two numbers (with zero-check)
- **Dependencies:** None (standard library only)
- **Use case:** Demonstrating multiple tool definitions
- **Test:** Ask Claude "What is 45 + 27?" or "Calculate 10 * 5"

### 3. Weather Server
**Pattern:** External API integration

- **Tool:** `get_weather` - Fetch weather and forecast for any location
- **API:** Open-Meteo (free, no auth required)
- **Data:** Current conditions + hourly forecast
- **Dependencies:** `requests` library
- **Use case:** Real-world API wrapping
- **Test:** Ask Claude "What's the weather in Berlin (52.52, 13.41)?" or provide any lat/lon

## Architecture

```
.mcp.json
├── Maps "echo" → echo-server/server.py
├── Maps "calculator" → calculator-server/server.py
└── Maps "weather" → weather-server/server.py
```

## Key Concepts

### Tool Definition
Each server declares available tools with:
- **name** - Unique identifier
- **description** - What the tool does
- **inputSchema** - JSON schema for input parameters

### Request/Response Pattern
- **Client sends:** `{"method": "tools/list"}` or `{"method": "tools/call", ...}`
- **Server returns:** Tool definitions or execution results

### External Integration
The weather server shows how to:
- Make HTTP requests to external APIs
- Parse JSON responses
- Format output for Claude

## Testing Locally

1. Install dependencies:
   ```bash
   pip install -r servers/weather-server/requirements.txt
   ```

2. Test individual servers:
   ```bash
   python servers/echo-server/server.py
   python servers/calculator-server/server.py
   python servers/weather-server/server.py
   ```

3. In Claude Code, use the tools naturally:
   - "Add 5 + 3"
   - "Echo hello"
   - "Get weather for latitude 40.7128, longitude -74.0060"

## What Makes This a Good Demo

✅ **Progression:** Echo (minimal) → Calculator (multiple tools) → Weather (external API)
✅ **Self-contained:** Each server works independently
✅ **Real-world:** Weather server is actually useful
✅ **Lightweight:** No complex dependencies or frameworks
✅ **Educational:** Shows the MCP pattern clearly
