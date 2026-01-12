# Migrating demo-commands to Marketplace Repository

This document explains how to migrate the demo-commands from this **development project** to your **marketplace-structured repository**.

## Overview

**Development Project** (you are here):
```
yw-claude-marketplace-development/
└── .claude/commands/
    ├── hello.md
    ├── greet.md
    ├── summarize.md
    ├── analyze-code.md
    ├── explain-code.md
    ├── check-types.md
    ├── test-report.md
    ├── TESTING.md
    └── MIGRATION.md (this file)
```

**Marketplace Repository** (destination):
```
yw-claude-marketplace-demo/
└── plugins/demo-commands/
    ├── plugin.json
    ├── README.md
    ├── commands/
    │   ├── hello.md
    │   ├── greet.md
    │   ├── summarize.md
    │   ├── analyze-code.md
    │   ├── explain-code.md
    │   ├── check-types.md
    │   └── test-report.md
    └── docs/
        └── TESTING.md
```

## Migration Steps

### Step 1: Copy Command Files

Copy all `.md` command files (not TESTING.md or MIGRATION.md) to the marketplace plugin:

```bash
# From: yw-claude-marketplace-development
# To: yw-claude-marketplace-demo/plugins/demo-commands/commands/

cp .claude/commands/hello.md ../yw-claude-marketplace-demo/plugins/demo-commands/commands/
cp .claude/commands/greet.md ../yw-claude-marketplace-demo/plugins/demo-commands/commands/
cp .claude/commands/summarize.md ../yw-claude-marketplace-demo/plugins/demo-commands/commands/
cp .claude/commands/analyze-code.md ../yw-claude-marketplace-demo/plugins/demo-commands/commands/
cp .claude/commands/explain-code.md ../yw-claude-marketplace-demo/plugins/demo-commands/commands/
cp .claude/commands/check-types.md ../yw-claude-marketplace-demo/plugins/demo-commands/commands/
cp .claude/commands/test-report.md ../yw-claude-marketplace-demo/plugins/demo-commands/commands/
```

Or as a batch:

```bash
cp .claude/commands/*.md ../yw-claude-marketplace-demo/plugins/demo-commands/commands/ \
  --exclude TESTING.md --exclude MIGRATION.md
```

### Step 2: Create plugin.json

Create `plugins/demo-commands/plugin.json` in the marketplace repo:

```json
{
  "name": "demo-commands",
  "version": "1.0.0",
  "description": "Hello World examples for Slash Commands extensibility"
}
```

### Step 3: Create README.md

Create `plugins/demo-commands/README.md` in the marketplace repo with user-facing documentation:

```markdown
# demo-commands - Slash Commands Demo

Hello World examples for Claude Code slash commands.

## Installation

\`\`\`bash
/plugin install demo-commands@yw-claude-marketplace-demo
\`\`\`

## Available Commands

| Command | Type | Example |
|---------|------|---------|
| `/hello` | Static prompt | `/hello` |
| `/greet` | With arguments | `/greet Alice` |
| `/summarize` | Project analysis | `/summarize` |
| `/analyze-code` | Code file analysis | `/analyze-code src/main.ts` |
| `/explain-code` | Code explanation | `/explain-code src/main.ts` |
| `/check-types` | TypeScript checker | `/check-types` |
| `/test-report` | Test suite runner | `/test-report` |

## What This Demonstrates

Each command shows a different slash command pattern:
- **Simple static prompts** (`/hello`)
- **Commands with arguments** (`/greet $ARGUMENTS`)
- **Multi-step workflows** (`/summarize`)
- **Tool integration** (`/check-types`, `/test-report`)

## How to Use

After installation, commands are available immediately:

1. Type `/` in Claude Code
2. Select a command from the autocomplete
3. Provide arguments if needed (shown with `$ARGUMENTS`)

## Examples

\`\`\`bash
/hello
→ Friendly greeting message

/greet Yoshi
→ Personalized greeting with fun facts about the name

/summarize
→ Analysis of the current project

/analyze-code src/main.ts
→ Analysis of the specified file
\`\`\`

## Testing

See TESTING.md in the plugin directory for detailed testing instructions.
```

### Step 4: Copy Testing Documentation

Optionally, copy testing docs:

```bash
cp .claude/commands/TESTING.md ../yw-claude-marketplace-demo/plugins/demo-commands/docs/
```

### Step 5: Update Marketplace Catalog

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
    // ... other plugins ...
  ]
}
```

### Step 6: Test in Marketplace

```bash
cd ../yw-claude-marketplace-demo

# Test locally
/plugin marketplace add file:///absolute/path/to/yw-claude-marketplace-demo
/plugin install demo-commands@yw-claude-marketplace-demo

# Test the commands
/hello
/greet TestUser
/summarize
```

### Step 7: Commit and Push

```bash
cd ../yw-claude-marketplace-demo
git add -A
git commit -m "Add demo-commands plugin - slash command examples"
git push origin main
```

## File Structure Reference

**Development Project** (.claude/commands/):
- Files are loose in the directory
- Includes TESTING.md and MIGRATION.md for developers
- Tested locally during development

**Marketplace Project** (plugins/demo-commands/):
- Commands in `commands/` subdirectory
- Proper plugin metadata (plugin.json)
- User-facing README.md
- Optional docs/ for additional resources

## Troubleshooting

### Commands not appearing after installation
- Check that command files are in the correct directory
- Verify file names don't have extra characters
- Restart Claude Code

### Commands with $ARGUMENTS not working
- Ensure the placeholder is exactly `$ARGUMENTS`
- Check file paths in the prompt are relative to project root

### Updating an Existing Plugin

If demo-commands is already in the marketplace:

1. Update command files in `.claude/commands/`
2. Test locally
3. Copy updated files to marketplace
4. Update `plugin.json` version number
5. Commit with message: "Update demo-commands: [what changed]"

## Questions?

Refer to:
- `TESTING.md` in this directory for testing details
- `development-plan.md` in the project root for context
- The marketplace README for general plugin information
