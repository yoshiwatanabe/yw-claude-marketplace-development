# MCP Server Dependency Setup Instructions

## Context
We have a demo marketplace (`yw-claude-marketplace-demo`) containing lightweight MCP server examples. These servers need their Python dependencies installed for end users, but we want the setup to be as simple and non-intrusive as possible.

## Goal
Create artifacts that enable end users to easily set up MCP server dependencies with minimal manual intervention.

## Recommended Approach: Vendored Dependencies

For our lightweight demo servers, we'll use **vendored dependencies** (bundling dependencies directly in the plugin). This is the simplest approach for end users because:

- No post-install scripts to run
- No virtual environments to manage
- No system Python environment pollution
- Works immediately after marketplace installation
- Portable across different Python installations

## Required Artifacts

Please create the following files to implement this approach:

### 1. **Setup Script: `scripts/vendor-dependencies.js`**

A Node.js script that:
- Iterates through each MCP server directory in `servers/`
- Checks for `requirements.txt` in each server
- Runs `pip install -r requirements.txt -t ./vendored` for each server
- Creates a `.gitignore` entry for vendored folders
- Provides clear console output about what's being installed

Requirements:
- Should work on Windows (WSL), macOS, and Linux
- Should check if Python/pip is available before attempting installation
- Should handle errors gracefully with helpful messages
- Should skip servers that don't have `requirements.txt`

### 2. **Server Wrapper Template: `servers/[server-name]/run.py`**

A Python wrapper script that:
- Adds the `./vendored` directory to `sys.path` before importing dependencies
- Then imports and runs the actual server code
- Should be generic enough to use across multiple servers

Example structure:
```python
import sys
import os

# Add vendored dependencies to path
vendor_dir = os.path.join(os.path.dirname(__file__), 'vendored')
if os.path.exists(vendor_dir):
    sys.path.insert(0, vendor_dir)

# Import and run the actual server
from server import main  # or whatever the server's entry point is
if __name__ == '__main__':
    main()
```

### 3. **Update MCP Server Configs**

The plugin's MCP server configuration should use `run.py` as the entry point instead of `server.py` directly.

Example configuration pattern:
```json
{
  "mcpServers": {
    "echo": {
      "command": "python",
      "args": ["./servers/echo-server/run.py"],
      "cwd": "${pluginDir}"
    }
  }
}
```

### 4. **Developer Setup Guide: `DEVELOPMENT.md`**

Documentation for marketplace developers (us) that explains:
- How to run the vendor script before publishing
- How to test that vendored dependencies work
- How to update dependencies
- What to include/exclude in version control

### 5. **End User Setup Guide: `README.md` (Update)**

Add a section explaining:
- That dependencies are pre-bundled (no setup needed!)
- Minimum Python version requirement (if any)
- Troubleshooting if something doesn't work

### 6. **Package.json Update**

Add a convenient npm script:
```json
{
  "scripts": {
    "prepare-mcp": "node scripts/vendor-dependencies.js",
    "test-mcp": "node scripts/test-mcp-servers.js"
  }
}
```

### 7. **Optional: Test Script: `scripts/test-mcp-servers.js`**

A script that:
- Attempts to start each MCP server
- Verifies they can import their dependencies
- Reports which servers are ready and which have issues
- Useful for both development and end-user troubleshooting

## Implementation Notes

### Current Server Structure
We have these servers in the demo:
- `servers/echo-server/` (server.py + requirements.txt)
- `servers/calculator/` (server.py + requirements.txt)
- `servers/weather/` (server.py + requirements.txt)

### Vendoring Process
For each server:
1. Navigate to server directory
2. Run: `pip install -r requirements.txt -t ./vendored`
3. Create wrapper `run.py` that adds vendored to path
4. Update plugin config to use `run.py` as entry point

### .gitignore Considerations
Add to `.gitignore`:
```
# Vendored dependencies (these get regenerated)
**/vendored/

# But DO commit vendored dependencies for distribution
# (comment out the above when preparing for release)
```

**Important**: For distribution, we WANT to commit the vendored folders so end users get them. But during development, we might want to exclude them.

## Edge Cases to Handle

1. **Platform-specific dependencies**: Some Python packages have compiled components. For truly portable distribution, we might need to vendor for each platform separately, or stick to pure-Python dependencies only.

2. **Dependency conflicts**: If multiple servers need different versions of the same package, vendoring per-server (our approach) handles this cleanly.

3. **Large dependencies**: If any demo server has heavy dependencies, we might want to reconsider that server for the demo or use a different approach.

## Success Criteria

End user experience should be:
1. Install marketplace: `claude marketplace install https://github.com/your-org/yw-claude-marketplace-demo`
2. Enable plugin: automatically enabled or via settings
3. Use MCP servers: they just work, no additional setup

## Questions for Claude Code

1. Should we vendor dependencies and commit them to the repo, or generate them during marketplace installation?
   - **Recommendation**: Commit them for simplest end-user experience

2. Do we need to handle multiple Python versions or platforms?
   - **Recommendation**: Test on Python 3.8+ (most common), pure-Python deps only

3. Should we provide a fallback mechanism if vendored deps don't work?
   - **Recommendation**: Add troubleshooting section in README with manual setup instructions

## Next Steps

1. Create the `vendor-dependencies.js` script
2. Create the `run.py` wrapper template
3. Update each server to use the wrapper
4. Run vendor script to populate dependencies
5. Update plugin MCP server configs
6. Test on fresh installation
7. Update documentation

Please implement these artifacts focusing on simplicity and reliability for end users.