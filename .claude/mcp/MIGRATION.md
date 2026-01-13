# Migrating demo-mcp to Marketplace Repository

This document explains how to migrate the MCP servers from this **development project** to your **marketplace-structured repository**.

## Overview

**Development Project** (you are here):
```
yw-claude-marketplace-development/
└── .claude/mcp/
    ├── .mcp.json
    ├── README.md
    ├── MIGRATION.md (this file)
    └── servers/
        ├── echo-server/
        │   ├── server.py
        │   └── requirements.txt
        ├── calculator-server/
        │   ├── server.py
        │   └── requirements.txt
        └── weather-server/
            ├── server.py
            └── requirements.txt
```

**Marketplace Repository** (destination):
```
yw-claude-marketplace-demo/
└── plugins/demo-mcp/
    ├── plugin.json
    ├── README.md
    ├── .mcp.json
    └── servers/
        ├── echo-server/
        │   ├── server.py
        │   └── requirements.txt
        ├── calculator-server/
        │   ├── server.py
        │   └── requirements.txt
        └── weather-server/
            ├── server.py
            └── requirements.txt
```

## Migration Steps

### Step 1: Copy MCP Servers Directory

Copy the entire `servers/` directory and `.mcp.json` to the marketplace plugin:

```bash
# From: yw-claude-marketplace-development
# To: yw-claude-marketplace-demo/plugins/demo-mcp/

cp -r .claude/mcp/servers ../yw-claude-marketplace-demo/plugins/demo-mcp/
cp .claude/mcp/.mcp.json ../yw-claude-marketplace-demo/plugins/demo-mcp/
```

Verify the structure in the marketplace:
```bash
ls -R ../yw-claude-marketplace-demo/plugins/demo-mcp/servers/
# Should show: echo-server/, calculator-server/, weather-server/
```

### Step 2: Create plugin.json

Create `plugins/demo-mcp/plugin.json` in the marketplace repo:

```json
{
  "name": "demo-mcp",
  "version": "1.0.0",
  "description": "Hello World examples for MCP Servers extensibility"
}
```

### Step 3: Create README.md

Create `plugins/demo-mcp/README.md` in the marketplace repo with user-facing documentation:

```markdown
# demo-mcp - MCP Servers Demo

Hello World examples for Claude Code MCP (Model Context Protocol) server integration.

## Installation

\`\`\`bash
/plugin install demo-mcp@yw-claude-marketplace-demo
\`\`\`

### Dependencies

The weather server requires the `requests` library:

\`\`\`bash
pip install requests
\`\`\`

(Or install all server dependencies: \`pip install -r plugins/demo-mcp/servers/weather-server/requirements.txt\`)

## Available Servers

| Server | Tools | Pattern | Dependencies |
|--------|-------|---------|---|
| **echo** | \`echo\` | Minimal MCP | None |
| **calculator** | \`add, subtract, multiply, divide\` | Multiple tools | None |
| **weather** | \`get_weather\` | External API integration | requests |

## What This Demonstrates

Each server shows a different MCP pattern:

- **echo-server** - Minimal MCP with a single tool
- **calculator-server** - Multiple tools in one server with error handling
- **weather-server** - Real-world API integration (Open-Meteo)

## How to Use

After installation, tools are available automatically in Claude Code.

### Echo Example
Ask Claude: "Echo hello world"
- Tool used: echo
- Response: "Echo: hello world"

### Calculator Example
Ask Claude: "What is 45 + 27?" or "Calculate 10 × 5"
- Tools used: add, multiply
- Handles division by zero gracefully

### Weather Example
Ask Claude: "What's the weather in Berlin?" or "Get weather for latitude 40.71, longitude -74.01"
- Tool used: get_weather
- Returns current conditions + 3-hour forecast
- Uses Open-Meteo API (no auth required)

## Architecture

### Server Configuration (.mcp.json)

Maps server names to Python executables:

```json
{
  "mcpServers": {
    "echo": {
      "command": "python",
      "args": ["${CLAUDE_PLUGIN_ROOT}/servers/echo-server/server.py"]
    },
    "calculator": {
      "command": "python",
      "args": ["${CLAUDE_PLUGIN_ROOT}/servers/calculator-server/server.py"]
    },
    "weather": {
      "command": "python",
      "args": ["${CLAUDE_PLUGIN_ROOT}/servers/weather-server/server.py"]
    }
  }
}
```

### Tool Definitions

Each server declares its tools with:
- **name** - Tool identifier
- **description** - What the tool does
- **inputSchema** - JSON Schema for parameters

Claude automatically discovers and uses these tools.

## Testing Locally

### List Available Tools

\`\`\`bash
# Test any server's tool definitions
echo '{"method": "tools/list"}' | python3 servers/echo-server/server.py
\`\`\`

### Call a Tool

\`\`\`bash
# Test calculator add
echo '{"method": "tools/call", "params": {"name": "add", "arguments": {"a": 15, "b": 27}}}' \\
  | timeout 1 python3 servers/calculator-server/server.py
# Response: {"content": [{"type": "text", "text": "Result: 42"}]}

# Test weather
echo '{"method": "tools/call", "params": {"name": "get_weather", "arguments": {"latitude": 52.52, "longitude": 13.41}}}' \\
  | timeout 3 python3 servers/weather-server/server.py
\`\`\`

## File Structure Reference

**Development Project** (.claude/mcp/):
- Servers are in active development
- Includes MIGRATION.md for developer reference
- Local testing during development

**Marketplace Project** (plugins/demo-mcp/):
- Servers in production structure
- Proper plugin metadata (plugin.json)
- User-facing README.md
- .mcp.json configured for marketplace paths

## Key Points

✅ Each server is **self-contained** and **independent**
✅ Servers use **standard Python** (no complex frameworks)
✅ All tested and **working examples**
✅ Progressive complexity: minimal → multiple tools → external API
✅ Error handling included (e.g., division by zero)

## Updating Servers

If you update a server in development:

1. Test it locally in the development project
2. Copy updated files to `plugins/demo-mcp/servers/`
3. Update `plugin.json` version number
4. Test in marketplace
5. Commit with message: "Update demo-mcp: [what changed]"

## Troubleshooting

### Server not found or not responding
- Check `.mcp.json` paths are correct
- Verify server files exist in the `servers/` directory
- Ensure Python 3 is available

### Weather server fails
- Install requests: \`pip install requests\`
- Check internet connectivity (API call to Open-Meteo)
- Verify latitude/longitude format (decimal degrees)

### Tool not working in Claude Code
- Restart Claude Code after plugin installation
- Check that `.mcp.json` is in the plugin root
- Verify server definitions in the Python files

## Questions?

Refer to:
- Server README in this directory for architecture details
- development-plan.md in the project root for context
- The marketplace README for general plugin information
