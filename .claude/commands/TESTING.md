# Testing Demo Commands

This document describes how to test the demo-commands locally in Claude Code.

## Available Commands

| Command | Type | Description |
|---------|------|-------------|
| `/hello` | Static | Simple greeting |
| `/greet` | With arguments | Personalized greeting with name facts |
| `/summarize` | Multi-step | Project analysis and summary |
| `/analyze-code` | With arguments | Analyze a specific code file |
| `/explain-code` | With arguments | Simple code explanation |
| `/check-types` | Runs tool | TypeScript type checking |
| `/test-report` | Runs tool | Test suite report |

## Testing Locally

In Claude Code, commands are automatically discovered from `.claude/commands/` directory.

### 1. Basic Commands (No Arguments)

```bash
/hello
```

Expected: Friendly greeting message.

```bash
/summarize
```

Expected: Analysis of the current project (will analyze this development sandbox).

### 2. Commands with Arguments

```bash
/greet Alice
```

Expected: Personalized greeting for "Alice".

```bash
/analyze-code .claude/skills/calculator/SKILL.md
```

Expected: Analysis of the file specified.

```bash
/explain-code .claude/commands/hello.md
```

Expected: Simple explanation of what the hello.md command does.

### 3. Commands That Interact with Tools

These will use Claude's tools to interact with the project:

```bash
/check-types
```

Note: Only works in projects with TypeScript setup.

```bash
/test-report
```

Note: Only works in projects with test suite configured.

## Testing Checklist

After making changes to any command file:

- [ ] Command appears in `/` autocomplete
- [ ] Command prompt makes sense
- [ ] Command executes without syntax errors
- [ ] Output is helpful and relevant
- [ ] $ARGUMENTS placeholder works correctly (if applicable)

## Command Examples

### /hello
- Input: `/hello`
- Should produce: Warm, friendly greeting specific to Claude Code demo

### /greet
- Input: `/greet Yoshi`
- Should produce: Personalized greeting with fun fact about the name

### /summarize
- Input: `/summarize`
- Should produce: Overview of this development sandbox project

### /analyze-code
- Input: `/analyze-code .claude/skills/calculator/SKILL.md`
- Should produce: Analysis of the calculator skill file

### /explain-code
- Input: `/explain-code .claude/commands/hello.md`
- Should produce: Simple explanation of how hello.md works

## Debugging

If a command doesn't appear:
1. Check the file is in `.claude/commands/` directory
2. Verify file extension is `.md`
3. Check for syntax errors in the prompt text
4. Reload Claude Code or restart the session

If a command produces errors:
1. Check for invalid $ARGUMENTS syntax
2. Verify the file path in $ARGUMENTS exists
3. Check for typos in the command prompt
