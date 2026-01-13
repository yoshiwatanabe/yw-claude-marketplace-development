#!/usr/bin/env node
/**
 * Vendor Dependencies Script for MCP Servers
 *
 * This script installs dependencies for each MCP server into a vendored directory.
 * Dependencies are installed per-server to avoid conflicts between servers.
 *
 * Usage: node scripts/vendor-dependencies.js
 */

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

// Colors for console output
const colors = {
  reset: '\x1b[0m',
  green: '\x1b[32m',
  red: '\x1b[31m',
  yellow: '\x1b[33m',
  blue: '\x1b[34m',
};

function log(message, color = 'reset') {
  console.log(`${colors[color]}${message}${colors.reset}`);
}

function checkPythonAvailable() {
  try {
    const version = execSync('python3 --version', { encoding: 'utf8' });
    log(`✓ Found Python: ${version.trim()}`, 'green');
    return true;
  } catch (error) {
    try {
      const version = execSync('python --version', { encoding: 'utf8' });
      log(`✓ Found Python: ${version.trim()}`, 'green');
      return true;
    } catch (err) {
      log('✗ Python not found. Please install Python 3.8+', 'red');
      return false;
    }
  }
}

function getPythonCommand() {
  try {
    execSync('python3 --version', { stdio: 'ignore' });
    return 'python3';
  } catch {
    return 'python';
  }
}

function getServersWithDependencies(serversDir) {
  const servers = [];

  if (!fs.existsSync(serversDir)) {
    log(`✗ Servers directory not found: ${serversDir}`, 'red');
    return servers;
  }

  const serverDirs = fs.readdirSync(serversDir);

  for (const serverName of serverDirs) {
    const serverPath = path.join(serversDir, serverName);
    const requirementsPath = path.join(serverPath, 'requirements.txt');

    // Check if it's a directory and has requirements.txt
    if (fs.statSync(serverPath).isDirectory() && fs.existsSync(requirementsPath)) {
      servers.push({
        name: serverName,
        path: serverPath,
        requirementsPath: requirementsPath
      });
    }
  }

  return servers;
}

function vendorDependencies(serverPath, requirementsPath, pythonCmd) {
  const vendoredDir = path.join(serverPath, 'vendored');

  try {
    log(`  Installing dependencies...`, 'blue');

    // Create vendored directory if it doesn't exist
    if (!fs.existsSync(vendoredDir)) {
      fs.mkdirSync(vendoredDir, { recursive: true });
    }

    // Run pip install with -t flag to install into vendored directory
    const command = `${pythonCmd} -m pip install -r "${requirementsPath}" -t "${vendoredDir}" --quiet`;

    execSync(command, {
      stdio: 'pipe',
      cwd: serverPath
    });

    log(`  ✓ Dependencies vendored to ${vendoredDir}`, 'green');
    return true;
  } catch (error) {
    log(`  ✗ Failed to vendor dependencies:`, 'red');
    log(`    ${error.message}`, 'red');
    return false;
  }
}

function main() {
  log('\n=== MCP Server Dependency Vendoring ===\n', 'blue');

  // Check Python availability
  if (!checkPythonAvailable()) {
    process.exit(1);
  }

  const pythonCmd = getPythonCommand();
  const serversDir = path.join(__dirname, '..', 'servers');

  // Find servers with requirements.txt
  const servers = getServersWithDependencies(serversDir);

  if (servers.length === 0) {
    log('\n✓ No servers with dependencies found (all using standard library only)', 'green');
    return;
  }

  log(`\nFound ${servers.length} server(s) with dependencies:\n`, 'blue');

  let successCount = 0;
  let failureCount = 0;

  for (const server of servers) {
    log(`Processing: ${server.name}`, 'yellow');

    const success = vendorDependencies(server.path, server.requirementsPath, pythonCmd);

    if (success) {
      successCount++;
    } else {
      failureCount++;
    }

    log('');
  }

  // Summary
  log('=== Summary ===', 'blue');
  log(`✓ Successfully vendored: ${successCount}`, 'green');

  if (failureCount > 0) {
    log(`✗ Failed: ${failureCount}`, 'red');
    process.exit(1);
  } else {
    log('\n✓ All dependencies vendored successfully!', 'green');
    log('Ready for distribution. Commit vendored directories to share dependencies with users.\n', 'green');
  }
}

main();
