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
    ├── scripts/
    │   └── vendor-dependencies.js
    └── servers/
        ├── echo-server/
        │   ├── server.py
        │   ├── run.py
        │   ├── requirements.txt
        │   └── vendored/
        │       └── .gitkeep
        ├── calculator-server/
        │   ├── server.py
        │   ├── run.py
        │   ├── requirements.txt
        │   └── vendored/
        │       └── .gitkeep
        └── weather-server/
            ├── server.py
            ├── run.py
            ├── requirements.txt
            └── vendored/
                ├── requests/
                ├── urllib3/
                ├── certifi/
                └── ...
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
        │   ├── run.py
        │   ├── requirements.txt
        │   └── vendored/
        │       └── .gitkeep
        ├── calculator-server/
        │   ├── server.py
        │   ├── run.py
        │   ├── requirements.txt
        │   └── vendored/
        │       └── .gitkeep
        └── weather-server/
            ├── server.py
            ├── run.py
            ├── requirements.txt
            └── vendored/
                ├── requests/
                ├── urllib3/
                ├── certifi/
                └── ...
```

## Key Innovation: Vendored Dependencies

Starting with this version, MCP servers use **vendored dependencies** - dependencies are bundled directly in the plugin. This means:

✅ End users don't need to run `pip install`
✅ No manual setup required
✅ Works immediately after installation
✅ Dependencies are isolated per server

The `run.py` wrapper in each server directory adds the vendored dependencies to Python's path before running the actual server.

## Migration Steps

### Step 0: Prepare Development Project (One-time Setup)

Before copying to marketplace, ensure vendored dependencies are prepared:

```bash
# Run this in the development project
node .claude/mcp/scripts/vendor-dependencies.js

# This will:
# 1. Find all servers with requirements.txt
# 2. Install dependencies into servers/[name]/vendored/
# 3. Create run.py wrappers (if not already present)
```

Commit the vendored directories so they're distributed with the plugin.

### Step 1: Copy MCP Servers Directory

Copy the entire `servers/` directory (including vendored dependencies!) and `.mcp.json` to the marketplace plugin:

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

### Step 2: Update .mcp.json for Marketplace Paths

The `.mcp.json` needs to be updated to reflect the different directory structure in the marketplace:

**Development** (.claude/mcp/.mcp.json):
```json
{
  "mcpServers": {
    "echo": {
      "command": "python",
      "args": ["${CLAUDE_PLUGIN_ROOT}/.claude/mcp/servers/echo-server/run.py"]
    }
  }
}
```

**Marketplace** (plugins/demo-mcp/.mcp.json):
```json
{
  "mcpServers": {
    "echo": {
      "command": "python",
      "args": ["${CLAUDE_PLUGIN_ROOT}/servers/echo-server/run.py"]
    }
  }
}
```

The key difference: remove the `.claude/mcp/` prefix since servers are at the plugin root in the marketplace.

### Step 3: Update Marketplace Catalog

In the marketplace repo, update `.claude-plugin/marketplace.json` to include the new plugin:

```json
{
  "name": "yw-claude-marketplace-demo",
  "description": "[DEMO] Claude extensibility features",
  "owner": { ... },
  "plugins": [
    {
      "name": "demo-commands",
      "source": "./plugins/demo-commands",
      "description": "Slash command patterns: simple, arguments, workflows"
    },
    {
      "name": "demo-mcp",
      "source": "./plugins/demo-mcp",
      "description": "MCP server patterns: minimal, multiple tools, external API"
    },
    // ... other plugins ...
  ]
}
```


### Step 4: Create plugin.json

Create `plugins/demo-mcp/plugin.json` in the marketplace repo:

```json
{
  "name": "demo-mcp",
  "version": "1.0.0",
  "description": "Hello World examples for MCP Servers extensibility"
}
```

### Step 5: Create README.md

Create `plugins/demo-mcp/README.md` in the marketplace repo with user-facing documentation:

```markdown
# demo-mcp - MCP Servers Demo

Hello World examples for Claude Code MCP (Model Context Protocol) server integration.

## Installation

\`\`\`bash
/plugin install demo-mcp@yw-claude-marketplace-demo
\`\`\`

### Dependencies

All dependencies are **pre-bundled** with the plugin using vendored dependencies. No manual installation required!

The plugin includes:
- weather-server: requests library (vendored)
- echo-server: Python standard library only
- calculator-server: Python standard library only

Just install and use - everything works out of the box.

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

### Step 6: Test in Marketplace

```bash
cd ../yw-claude-marketplace-demo

# Test locally
/plugin marketplace add file:///absolute/path/to/yw-claude-marketplace-demo
/plugin install demo-mcp@yw-claude-marketplace-demo

# Test the servers
# In Claude Code, try:
# "Echo hello"
# "What is 15 + 27?"
# "What's the weather in Berlin (52.52, 13.41)?"
```

### Step 7: Commit and Push

```bash
cd ../yw-claude-marketplace-demo
git add -A
git commit -m "Add demo-mcp plugin - MCP server examples"
git push origin main
```

## Architecture

### Server Configuration (.mcp.json)

Maps server names to Python executables via the `run.py` wrappers:

```json
{
  "mcpServers": {
    "echo": {
      "command": "python",
      "args": ["${CLAUDE_PLUGIN_ROOT}/servers/echo-server/run.py"]
    },
    "calculator": {
      "command": "python",
      "args": ["${CLAUDE_PLUGIN_ROOT}/servers/calculator-server/run.py"]
    },
    "weather": {
      "command": "python",
      "args": ["${CLAUDE_PLUGIN_ROOT}/servers/weather-server/run.py"]
    }
  }
}
```

**Important:** Entry points must use `run.py` (the wrapper), not `server.py`. The wrapper ensures vendored dependencies are added to Python's path before the actual server code runs.

### Tool Definitions

Each server declares its tools with:
- **name** - Tool identifier
- **description** - What the tool does
- **inputSchema** - JSON Schema for parameters

Claude automatically discovers and uses these tools.

## Testing Locally

### List Available Tools

\`\`\`bash
# Test any server's tool definitions using the run.py wrapper
echo '{"method": "tools/list"}' | python3 servers/echo-server/run.py
\`\`\`

### Call a Tool

\`\`\`bash
# Test calculator add
echo '{"method": "tools/call", "params": {"name": "add", "arguments": {"a": 15, "b": 27}}}' \\
  | timeout 1 python3 servers/calculator-server/run.py
# Response: {"content": [{"type": "text", "text": "Result: 42"}]}

# Test weather
echo '{"method": "tools/call", "params": {"name": "get_weather", "arguments": {"latitude": 52.52, "longitude": 13.41}}}' \\
  | timeout 3 python3 servers/weather-server/run.py
\`\`\`

**Note:** Always use `run.py` when testing, not `server.py`. The wrapper ensures vendored dependencies are available.

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
