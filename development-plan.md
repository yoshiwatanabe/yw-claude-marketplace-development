# Claude Extensibility Demos - Development Sandbox

> **Repository:** `yw-claude-marketplace-development` (Development Sandbox)
> **What This Is:** Temporary working directory for developing and testing Claude extensibility feature demos
> **Purpose:** Create working "Hello World" examples for all Claude extensibility features (Skills, MCP, Hooks, Triggers, etc.)
> **Workflow:** Develop → Test → Verify in this project → Copy to `yw-claude-marketplace-demo` → Publish to marketplace
> **Key Concept:** ONE marketplace repository will deliver MULTIPLE feature demos
> **Goal:** Breadth over depth - low-cognitive-load, hands-on learning samples
> **Audience:** Myself (and future marketplace users)

---

## 🔌 Development Workflow: From Sandbox to Marketplace

This repo is a **temporary development environment** for creating Claude extensibility demos:

### The Workflow
1. **Develop & Test** (in this repo)
   - Create feature demos in organized plugin structure
   - Test each extensibility feature (Skills, MCP, Hooks, etc.)
   - Verify with Claude Code

2. **Copy to Marketplace** (when ready to publish)
   - Mirror completed demo to `yw-claude-marketplace-demo` repository
   - This repo becomes the official distribution point for users

3. **Publish & Install** (end user workflow)
   ```bash
   # Users add the marketplace (from Claude Code)
   /plugin marketplace add https://github.com/yoshiwatanabe/yw-claude-marketplace-demo.git

   # List available demo plugins
   /plugin

   # Install a specific demo plugin
   /plugin install demo-skills@yw-claude-marketplace-demo
   ```

**Key Learning:** A single marketplace repository can distribute MULTIPLE demo plugins!

### Repository Structure

```
yw-claude-marketplace-development/     ← YOU ARE HERE (development sandbox)
├── development-plan.md                # This file - what we're building
├── README.md                          # Overview of development sandbox
├── brainstorming/                     # Planning & research notes
│
└── plugins/                           # Demo plugins in development
    ├── demo-claudemd/                 # Demo 01: CLAUDE.md patterns
    ├── demo-skills/                   # Demo 02: Skills examples
    ├── demo-mcp/                      # Demo 03: MCP Server examples
    ├── demo-commands/                 # Demo 04: Slash Commands
    ├── demo-subagents/                # Demo 05: Subagents
    ├── demo-hooks/                    # Demo 06: Hooks (event-driven automation)
    ├── demo-triggers/                 # Demo 07: Triggers (another hook pattern)
    ├── demo-full-plugin/              # Demo 08: Complete example
    ├── demo-thinking/                 # Demo 09: Extended thinking
    ├── demo-settings/                 # Demo 10: Configuration patterns
    └── demo-model-routing/            # Demo 11: LiteLLM integration

WHEN READY TO PUBLISH:
↓
yw-claude-marketplace-demo/            ← Destination marketplace repo
├── .claude-plugin/
│   └── marketplace.json               # Published catalog
├── README.md                          # User-facing marketplace docs
└── plugins/                           # Same structure, published demos
    ├── demo-skills/
    ├── demo-mcp/
    └── ... (copied from development)
```

---

## Environment Notes

| Environment | Best For | Features Available |
|-------------|----------|-------------------|
| **VS Code + Copilot** | Skills, MCP Servers | Skills (via Copilot), MCP Servers, some Copilot-specific features |
| **Claude Code (CLI)** | Full extensibility | All 7 mechanisms (Skills, MCP, Commands, Subagents, Hooks, Plugins, CLAUDE.md) |

> 📝 For features only in Claude Code, switch to WSL where Claude Code is installed.

---

## Claude Extensibility Features Overview

This development sandbox will create working "Hello World" demos for all Claude extensibility mechanisms:

### Core Extensibility Features

| # | Feature | What It Does | Plugin Name | Status |
|---|---------|--------------|-------------|--------|
| 1 | **Agent Skills** | Auto-triggered workflows with progressive disclosure | `demo-skills` | ☐ Todo |
| 2 | **Slash Commands** | Manual prompts triggered by user input | `demo-commands` | ☐ Todo |
| 3 | **MCP Servers** | Model Context Protocol for tool/resource integration | `demo-mcp` | ☐ Todo |
| 4 | **Subagents** | Isolated agents with separate context & tools | `demo-subagents` | ☐ Todo |
| 5 | **Hooks** | Event-driven automation (pre/post tool use, etc.) | `demo-hooks` | ☐ Todo |
| 6 | **Triggers** | Webhook-style event handlers | `demo-triggers` | ☐ Todo |
| 7 | **CLAUDE.md** | Project-scoped context file | `demo-claudemd` | ☐ Todo |

### Additional Features

| # | Feature | What It Does | Plugin Name | Status |
|---|---------|--------------|-------------|--------|
| 8 | **Extended Thinking** | Give Claude more compute for complex problems | `demo-thinking` | ☐ Todo |
| 9 | **Settings** | Project/user/plugin configuration hierarchy | `demo-settings` | ☐ Todo |
| 10 | **Model Routing** | Use different LLMs (GPT-4, Gemini, etc.) | `demo-model-routing` | ☐ Todo |
| 11 | **Complete Plugin** | All features working together | `demo-full-plugin` | ☐ Todo |

---

## Development Approach: "Hello World" for Each Feature

Each demo plugin follows the same philosophy:
- **Single Feature Focus**: Each plugin demonstrates ONE extensibility feature
- **Low Cognitive Load**: Minimal complexity - just enough to learn the concept
- **Working Examples**: Code that actually runs and works
- **Progressive Disclosure**: Start simple, show advanced patterns
- **Self-Contained**: Each demo is standalone and testable
- **Well-Documented**: Includes README with test scenarios

### What Each Demo Should Include

```
demo-feature/
├── plugin.json              # Plugin metadata
├── README.md                # Installation & test instructions
├── SKILL.md                 # (If skills) Skill definition
├── AGENT.md                 # (If agents) Agent definition
├── .mcp.json                # (If MCP) Server configuration
├── commands/                # (If commands) Slash commands
├── hooks/                   # (If hooks) Hook configurations
├── skills/                  # (If skills) Skill definitions
├── servers/                 # (If MCP) Server implementations
├── agents/                  # (If agents) Agent definitions
└── references/              # Documentation & examples
    ├── simple-example.md
    └── advanced-pattern.md
```

### Testing Each Demo

After development, each demo should be tested in this project:
1. ✓ Plugin loads without errors
2. ✓ Feature works as documented
3. ✓ Examples in README run successfully
4. ✓ No unexpected dependencies
5. ✓ README is clear and helpful

Once verified, it's ready to copy to the marketplace repo.

---

## Detailed Plugin Implementations

---

## Plugin 01: demo-claudemd - CLAUDE.md Patterns

**Feature:** Project-scoped always-on context  
**Install:** `/plugin install demo-claudemd@yw-claude-marketplace-demo`  
**Cognitive Load:** ⭐ Very Low

> ⚠️ **Note:** CLAUDE.md itself can't be distributed via plugin (it's a project file).  
> This plugin provides **example CLAUDE.md templates** as skills + reference docs.

### Plugin Structure

```
plugins/demo-claudemd/
├── plugin.json                  # Plugin metadata
├── README.md                    # Demo instructions
├── skills/
│   └── claudemd-templates/
│       ├── SKILL.md             # "Generate CLAUDE.md for this project"
│       └── references/
│           ├── minimal.md       # Minimal template
│           ├── tech-stack.md    # Tech stack template
│           ├── with-commands.md # With commands template
│           ├── with-conventions.md # With coding rules
│           └── full-example.md  # Complete example
└── commands/
    └── generate-claudemd.md     # /generate-claudemd command
```

### What to Demonstrate

- [ ] **Template: Minimal** - Just project name + description
- [ ] **Template: Tech Stack** - Next.js + Prisma + Tailwind declaration
- [ ] **Template: Commands** - npm scripts, make targets documentation
- [ ] **Template: Conventions** - Coding standards, file naming rules
- [ ] **Template: Full** - Complete example with all sections
- [ ] **Skill** - Auto-generate CLAUDE.md based on project analysis
- [ ] **Command** - `/generate-claudemd` to create one manually

### Test Scenarios

1. Install plugin, run `/generate-claudemd`
2. Ask "Create a CLAUDE.md for this project"
3. Skill should analyze project and generate appropriate CLAUDE.md

---

## Plugin 02: demo-skills - Skills Examples

**Feature:** Progressive-disclosure knowledge files  
**Install:** `/plugin install demo-skills@yw-claude-marketplace-demo`  
**Cognitive Load:** ⭐⭐ Low

### Plugin Structure

```
plugins/demo-skills/
├── plugin.json
├── README.md
├── skills/
│   ├── minimal-skill/
│   │   └── SKILL.md             # Simplest possible skill
│   ├── skill-with-references/
│   │   ├── SKILL.md
│   │   └── references/
│   │       └── guidelines.md    # Referenced documentation
│   ├── skill-with-scripts/
│   │   ├── SKILL.md
│   │   └── scripts/
│   │       └── helper.py        # Executable script
│   ├── skill-with-assets/
│   │   ├── SKILL.md
│   │   └── assets/
│   │       └── config.json      # Bundled data file
│   └── greeting-skill/
│       └── SKILL.md             # "When user says hello, respond warmly"
```

### What to Demonstrate

- [ ] **Minimal Skill** - SKILL.md with just description + workflow
- [ ] **With References** - Skill that loads reference docs on demand
- [ ] **With Scripts** - Skill that executes Python/Bash scripts
- [ ] **With Assets** - Skill with bundled JSON/template files
- [ ] **Auto-trigger** - Skill that activates on keyword detection

### Test Scenarios

1. Install plugin
2. Say "hello" → greeting-skill should auto-trigger
3. Ask about something matching skill descriptions
4. Verify progressive disclosure (metadata → content → resources)

---

## Plugin 03: demo-mcp - MCP Server Examples

**Feature:** Model Context Protocol for tool integration  
**Install:** `/plugin install demo-mcp@yw-claude-marketplace-demo`  
**Cognitive Load:** ⭐⭐⭐ Medium

### Plugin Structure

```
plugins/demo-mcp/
├── plugin.json
├── README.md
├── .mcp.json                    # MCP server configurations
├── servers/
│   ├── echo-server/
│   │   ├── server.py            # Minimal: just echoes input
│   │   └── requirements.txt
│   ├── calculator-server/
│   │   ├── server.py            # add, subtract, multiply tools
│   │   └── requirements.txt
│   ├── file-info-server/
│   │   ├── server.py            # get_file_info, list_directory
│   │   └── requirements.txt
│   └── weather-server/
│       ├── server.py            # Uses env var for API key
│       ├── requirements.txt
│       └── .env.example         # Template for credentials
```

### .mcp.json Configuration

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
    "file-info": {
      "command": "python",
      "args": ["${CLAUDE_PLUGIN_ROOT}/servers/file-info-server/server.py"]
    },
    "weather": {
      "command": "python",
      "args": ["${CLAUDE_PLUGIN_ROOT}/servers/weather-server/server.py"],
      "env": {
        "WEATHER_API_KEY": "${WEATHER_API_KEY}"
      }
    }
  }
}
```

### What to Demonstrate

- [ ] **Echo Server** - Minimal MCP (single tool, returns input)
- [ ] **Calculator Server** - Multiple tools in one server
- [ ] **File Info Server** - Tools that interact with filesystem
- [ ] **Weather Server** - Tool requiring environment variable credentials
- [ ] **MCP with Resources** - Expose data as MCP resources
- [ ] **MCP with Prompts** - Provide prompt templates via MCP

### Test Scenarios

1. Install plugin, run `/mcp` to see servers
2. Ask "what is 2 + 3?" → calculator should be used
3. Ask "echo hello world" → echo server
4. Verify env var handling with weather server

---

## Plugin 04: demo-commands - Slash Commands

**Feature:** User-triggered saved prompts  
**Install:** `/plugin install demo-commands@yw-claude-marketplace-demo`  
**Cognitive Load:** ⭐ Very Low

### Plugin Structure

```
plugins/demo-commands/
├── plugin.json
├── README.md
├── commands/
│   ├── hello.md                 # Simplest: just "Say hello"
│   ├── greet.md                 # With $ARGUMENTS: "Greet $ARGUMENTS"
│   ├── analyze-file.md          # "Analyze the file: $ARGUMENTS"
│   ├── summarize.md             # Multi-step workflow
│   ├── with-skill-ref.md        # References a skill
│   └── with-subagent.md         # Invokes a subagent
```

### Example Commands

**commands/hello.md:**
```markdown
Say "Hello from demo-commands plugin!" in a friendly way.
```

**commands/greet.md:**
```markdown
Please greet $ARGUMENTS warmly. Include a fun fact about their name if possible.
```

**commands/summarize.md:**
```markdown
Summarize the current project:

1. Read CLAUDE.md if it exists
2. List the main directories
3. Identify the tech stack
4. Provide a 3-sentence summary
```

### What to Demonstrate

- [ ] **Simple Command** - Just a static prompt
- [ ] **With Arguments** - Using $ARGUMENTS placeholder
- [ ] **Multi-step** - Workflow with numbered steps
- [ ] **Skill Reference** - Command that leverages a skill
- [ ] **Subagent Invocation** - Command that uses a subagent

### Test Scenarios

1. Install plugin
2. Type `/` and see new commands in autocomplete
3. Run `/hello`
4. Run `/greet Yoshi`
5. Run `/summarize`

---

## Plugin 05: demo-subagents - Subagent Examples

**Feature:** Isolated agents with separate context  
**Install:** `/plugin install demo-subagents@yw-claude-marketplace-demo`  
**Cognitive Load:** ⭐⭐ Low

### Plugin Structure

```
plugins/demo-subagents/
├── plugin.json
├── README.md
├── agents/
│   ├── minimal-agent/
│   │   └── AGENT.md             # Simplest possible agent
│   ├── reader-agent/
│   │   └── AGENT.md             # Only Read, Grep, Glob tools
│   ├── writer-agent/
│   │   └── AGENT.md             # Read + Write + Edit tools
│   ├── haiku-agent/
│   │   └── AGENT.md             # Uses claude-haiku model
│   ├── skilled-agent/
│   │   └── AGENT.md             # References skills
│   └── researcher/
│       └── AGENT.md             # Web research specialist
```

### Example Agent Definition

**agents/minimal-agent/AGENT.md:**
```markdown
---
name: minimal-agent
description: A minimal demonstration agent
tools: Read
---

You are a simple helper agent. 
When asked to do something, acknowledge the request and complete it.
```

**agents/haiku-agent/AGENT.md:**
```markdown
---
name: haiku-agent
description: Fast responses using Claude Haiku
model: claude-haiku-4-5-20251001
tools: Read, Grep
---

You are a fast helper optimized for quick responses.
Keep answers concise and efficient.
```

### What to Demonstrate

- [ ] **Minimal Agent** - Simplest AGENT.md
- [ ] **Limited Tools** - Agent with restricted tool access
- [ ] **Different Model** - Agent using Haiku for speed/cost
- [ ] **With Skills** - Agent that references skills
- [ ] **Parallel Agents** - Multiple agents working together

### Test Scenarios

1. Install plugin
2. Ask "use minimal-agent to read README.md"
3. Observe context isolation
4. Compare haiku-agent speed vs default

---

## Plugin 06: demo-hooks - Event-Driven Automation

**Feature:** Deterministic shell commands on lifecycle events  
**Install:** `/plugin install demo-hooks@yw-claude-marketplace-demo`  
**Cognitive Load:** ⭐⭐⭐ Medium

### Plugin Structure

```
plugins/demo-hooks/
├── plugin.json
├── README.md
├── hooks/
│   └── settings.json            # Hook configurations
├── scripts/
│   ├── log-session.sh           # Log session start
│   ├── format-file.sh           # Format edited files
│   ├── notify.sh                # Desktop notification
│   └── validate-edit.sh         # Validate before write
```

### Example hooks/settings.json

```json
{
  "hooks": {
    "SessionStart": [
      {
        "type": "command",
        "command": "${CLAUDE_PLUGIN_ROOT}/scripts/log-session.sh"
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Edit",
        "hooks": [
          {
            "type": "command",
            "command": "echo 'File edited: ${file}'"
          }
        ]
      }
    ],
    "PreToolUse": [
      {
        "matcher": "Write",
        "hooks": [
          {
            "type": "command",
            "command": "${CLAUDE_PLUGIN_ROOT}/scripts/validate-edit.sh ${file}"
          }
        ]
      }
    ]
  }
}
```

### What to Demonstrate

- [ ] **SessionStart Hook** - Log when session begins
- [ ] **PostToolUse Hook** - Action after file edits
- [ ] **PreToolUse Hook** - Validate/block before actions
- [ ] **PermissionRequest Hook** - Auto-approve patterns
- [ ] **Notification Hook** - Desktop notification

### Test Scenarios

1. Install plugin
2. Start new session → see log output
3. Edit a file → see post-edit hook run
4. Try to write to blocked file → see pre-hook block

---

## Plugin 07: demo-full-plugin - Complete Example

**Feature:** All components bundled together  
**Install:** `/plugin install demo-full-plugin@yw-claude-marketplace-demo`  
**Cognitive Load:** ⭐⭐⭐ Medium

### Plugin Structure

```
plugins/demo-full-plugin/
├── plugin.json
├── README.md
├── .mcp.json                    # MCP servers
├── skills/
│   └── project-analyzer/
│       ├── SKILL.md
│       └── references/
│           └── analysis-template.md
├── commands/
│   └── analyze.md               # /analyze command
├── agents/
│   └── analyzer/
│       └── AGENT.md             # Analysis subagent
├── hooks/
│   └── settings.json            # Hooks configuration
└── servers/
    └── project-info/
        └── server.py            # MCP server for project info
```

### What to Demonstrate

- [ ] **All 6 components** in one plugin
- [ ] **Component interaction** - skill uses MCP, command uses skill
- [ ] **Proper plugin.json** - Complete metadata
- [ ] **README** - Installation and usage docs

### Test Scenarios

1. Install plugin
2. Verify all components loaded
3. Test each component works
4. Test components work together

---

## Plugin 08: demo-thinking - Extended Thinking

**Feature:** Give Claude more compute time  
**Install:** `/plugin install demo-thinking@yw-claude-marketplace-demo`  
**Cognitive Load:** ⭐ Very Low

### Plugin Structure

```
plugins/demo-thinking/
├── plugin.json
├── README.md
├── commands/
│   ├── think.md                 # Trigger "think" mode
│   ├── think-hard.md            # Trigger "think hard" mode
│   └── ultrathink.md            # Trigger "ultrathink" mode
├── skills/
│   └── complex-reasoning/
│       ├── SKILL.md             # When to use extended thinking
│       └── references/
│           └── test-problems.md # Example problems
```

### What to Demonstrate

- [ ] **Think triggers** - "think", "think hard", "ultrathink"
- [ ] **Problem types** - When extended thinking helps
- [ ] **Comparison** - Same problem with/without thinking

---

## Plugin 10: demo-settings - Configuration Patterns

**Feature:** Project/user/plugin settings  
**Install:** `/plugin install demo-settings@yw-claude-marketplace-demo`  
**Cognitive Load:** ⭐⭐ Low

### Plugin Structure

```
plugins/demo-settings/
├── plugin.json
├── README.md
├── skills/
│   └── settings-explainer/
│       ├── SKILL.md             # Explain settings hierarchy
│       └── references/
│           ├── project-settings.md
│           ├── user-settings.md
│           └── env-vars.md
├── commands/
│   └── show-settings.md         # Display current settings
├── examples/
│   ├── project-settings.json    # Example .claude/settings.json
│   ├── user-settings.json       # Example ~/.claude/settings.json
│   └── local-settings.json      # Example .claude/settings.local.json
```

---

## Plugin 11: demo-model-routing - LiteLLM Integration

**Feature:** Use different LLMs with Claude Code  
**Install:** `/plugin install demo-model-routing@yw-claude-marketplace-demo`  
**Cognitive Load:** ⭐⭐⭐ Medium

### Plugin Structure

```
plugins/demo-model-routing/
├── plugin.json
├── README.md
├── .mcp.json                    # External LLM tools via MCP
├── skills/
│   └── multi-model/
│       ├── SKILL.md             # When to use which model
│       └── references/
│           └── model-comparison.md
├── agents/
│   ├── gpt-agent/
│   │   └── AGENT.md             # model: gpt-4o (via LiteLLM)
│   ├── gemini-agent/
│   │   └── AGENT.md             # model: gemini-pro
│   └── haiku-agent/
│       └── AGENT.md             # model: claude-haiku (fast/cheap)
├── servers/
│   └── external-llm/
│       ├── server.py            # MCP server calling external LLMs
│       └── requirements.txt
├── config/
│   ├── litellm_config.yaml      # LiteLLM proxy configuration
│   └── start-proxy.sh           # Start LiteLLM proxy
```

### What to Demonstrate

- [ ] **LiteLLM Setup** - Proxy configuration
- [ ] **Model Aliases** - gpt-4o, gemini-pro, claude-haiku
- [ ] **Subagent Routing** - Different models per agent
- [ ] **MCP Tool** - Call external LLMs as tools
- [ ] **Cost Comparison** - When to use which tier

---

## Standalone Demos (Not Plugins)

Some features can't be distributed as plugins or are better as standalone references:

### standalone/headless-mode/

**Feature:** CI/CD integration with Claude Code  
**Not a plugin because:** Headless mode is about running Claude, not extending it

```
standalone/headless-mode/
├── README.md
├── basic-usage.sh               # claude -p "prompt" --print
├── stream-json.sh               # --output-format stream-json
├── with-allowed-tools.sh        # --allowedTools Read,Grep
├── github-actions/
│   └── claude-review.yml        # PR review workflow
└── azure-pipelines/
    └── azure-pipelines.yml      # Azure DevOps workflow
```

### standalone/vscode-mcp/

**Feature:** MCP configuration in VS Code  
**Not a plugin because:** VS Code uses different config mechanism

```
standalone/vscode-mcp/
├── README.md
├── user-settings-example.json   # User-level MCP config
├── workspace-settings-example.json # Workspace-level MCP
└── servers/
    └── echo-server.py           # Same server, VS Code config
```

### standalone/user-level/

**Feature:** User-level skills/commands/agents  
**Not a plugin because:** Demonstrates ~/.claude/ usage

```
standalone/user-level/
├── README.md                    # Instructions for ~/.claude/
├── example-skills/              # Copy to ~/.claude/skills/
├── example-commands/            # Copy to ~/.claude/commands/
└── example-agents/              # Copy to ~/.claude/agents/
```

---

## Marketplace Configuration

### .claude-plugin/marketplace.json

```json
{
  "name": "yw-claude-marketplace-demo",
  "description": "[DEMO] Claude marketplace package showing working structure, metadata layout, and live Claude Skills",
  "owner": {
    "name": "Yoshi Watanabe",
    "email": "yoshiwatanabe@users.noreply.github.com"
  },
  "plugins": [
    {
      "name": "demo-claudemd",
      "source": "./plugins/demo-claudemd",
      "description": "CLAUDE.md template generator and examples"
    },
    {
      "name": "demo-skills",
      "source": "./plugins/demo-skills",
      "description": "Skill patterns: minimal, references, scripts, assets"
    },
    {
      "name": "demo-mcp",
      "source": "./plugins/demo-mcp",
      "description": "MCP server examples: echo, calculator, with env vars"
    },
    {
      "name": "demo-commands",
      "source": "./plugins/demo-commands",
      "description": "Slash command patterns: simple, arguments, workflows"
    },
    {
      "name": "demo-subagents",
      "source": "./plugins/demo-subagents",
      "description": "Subagent patterns: minimal, limited tools, different models"
    },
    {
      "name": "demo-hooks",
      "source": "./plugins/demo-hooks",
      "description": "Hook patterns: pre/post tool use, session events"
    },
    {
      "name": "demo-full-plugin",
      "source": "./plugins/demo-full-plugin",
      "description": "Complete plugin with all 6 components"
    },
    {
      "name": "demo-thinking",
      "source": "./plugins/demo-thinking",
      "description": "Extended thinking triggers and examples"
    },
    {
      "name": "demo-settings",
      "source": "./plugins/demo-settings",
      "description": "Settings hierarchy and configuration patterns"
    },
    {
      "name": "demo-model-routing",
      "source": "./plugins/demo-model-routing",
      "description": "LiteLLM integration for multi-model routing"
    }
  ]
}
```

---

## Quick Reference Card

```
┌──────────────────────────────────────────────────────────────────┐
│                    CLAUDE EXTENSIBILITY                          │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  CLAUDE.md      → Always-on context (project constitution)      │
│  Skills         → Auto-triggered workflows (.claude/skills/)    │
│  MCP Servers    → External tools/data (.mcp.json)               │
│  Slash Commands → Manual prompts (.claude/commands/)            │
│  Subagents      → Isolated agents (.claude/agents/)             │
│  Hooks          → Event automation (.claude/settings.json)      │
│  Plugins        → Bundle everything (.claude-plugin/)           │
│                                                                  │
├──────────────────────────────────────────────────────────────────┤
│  Extended Thinking → "think" / "think hard" / "ultrathink"      │
│  Headless Mode     → claude -p "prompt" --print                 │
│  Model Routing     → LiteLLM / ANTHROPIC_BASE_URL               │
│  VS Code MCP       → settings.json > mcp.servers                │
└──────────────────────────────────────────────────────────────────┘
```

---

---

## Publication & Migration Workflow

When a demo is **verified and working** in this development sandbox:

### Step 1: Verify in Development
```bash
# In this repo (yw-claude-marketplace-development)
/plugin install demo-skills  # Test it works locally
```

### Step 2: Copy to Marketplace
```bash
# After verification, copy the demo plugin to the marketplace repo
cp -r plugins/demo-skills ../yw-claude-marketplace-demo/plugins/

# Update marketplace.json in the destination repo
# Add entry for the new demo to .claude-plugin/marketplace.json
```

### Step 3: Test in Marketplace
```bash
# In marketplace repo (yw-claude-marketplace-demo)
/plugin marketplace add file:///path/to/yw-claude-marketplace-demo
/plugin install demo-skills@yw-claude-marketplace-demo
```

### Step 4: Publish
```bash
# Commit and push the marketplace repo to GitHub
cd ../yw-claude-marketplace-demo
git add -A
git commit -m "Add demo-skills to marketplace"
git push origin main
```

---

## Implementation Priority

### Phase 1: Bootstrap Development Sandbox (Do First!)
1. ☐ Create `plugins/` directory structure
2. ☐ Create root `README.md` for this sandbox
3. ☐ Create first demo skeleton

### Phase 2: Core Plugins (Foundations)
4. ☐ Plugin 1: demo-skills (most fundamental - Agent Skills)
5. ☐ Plugin 2: demo-commands (very easy - Slash Commands)
6. ☐ Plugin 3: demo-mcp (medium complexity - MCP Servers)

### Phase 3: Advanced Plugins
7. ☐ Plugin 4: demo-subagents
8. ☐ Plugin 5: demo-hooks
9. ☐ Plugin 6: demo-triggers (if different from hooks)
10. ☐ Plugin 7: demo-claudemd (CLAUDE.md templates)

### Phase 4: Complete & Additional Features
11. ☐ Plugin 8: demo-full-plugin (all components together)
12. ☐ Plugin 9: demo-thinking (extended thinking)
13. ☐ Plugin 10: demo-settings (configuration)
14. ☐ Plugin 11: demo-model-routing (LiteLLM)

---

## Getting Started (Development)

### Step 1: Set up the development sandbox structure

```bash
cd yw-claude-marketplace-development

# Create plugins directory (if not already present)
mkdir -p plugins

# Create first demo plugin structure
mkdir -p plugins/demo-skills/skills
mkdir -p plugins/demo-commands/commands
mkdir -p plugins/demo-mcp/servers
```

### Step 2: Create your first demo plugin

Start with `demo-skills` - it's the most fundamental extensibility feature.

Create: `plugins/demo-skills/plugin.json`
```json
{
  "name": "demo-skills",
  "version": "1.0.0",
  "description": "Hello World examples for Agent Skills"
}
```

### Step 3: Develop and test in this project

```bash
# In Claude Code (WSL/local)
/plugin install demo-skills  # Install from local directory
# Test the feature...
# Verify it works as documented
```

### Step 4: When ready to publish

See "Publication & Migration Workflow" section above to copy to marketplace repo.

---

## Initial Setup Files

For the first time setup, create these files:

### 1. README.md (Development Sandbox)

Create at the root to document this development environment.

### 2. plugins/demo-skills/plugin.json

```json
{
  "name": "demo-skills",
  "version": "1.0.0",
  "description": "Hello World examples for Agent Skills extensibility"
}
```

### 3. plugins/demo-skills/README.md

Create with instructions on testing the Agent Skills demo.

---

## Notes

- This is a **temporary development environment** for creating and testing demo features
- Each demo is self-contained and independently testable via `/plugin install`
- When verified and documented, demos are copied to `yw-claude-marketplace-demo` for publication
- Experiment freely and iterate rapidly here before publishing
- See "Publication & Migration Workflow" section for how to publish completed demos