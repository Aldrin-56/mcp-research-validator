# Research Validator MCP Server

An MCP (Model Context Protocol) Server delivering the **Self-Validating Academic Research Framework**. 
This pure-AI cognitive extension injects strict hallucination-prevention constraints into any MCP-compatible AI agent (Claude Desktop, Cursor, Antigravity, etc.).

## What this does
It natively alters the AI's internal cognition loop, forcing standard 3-Layer Validation (Pre-Action Anchor, In-Flight Halt, Post-Action semantic auto-revert). It prevents the AI from inventing algorithms, bypassing academic formalisms, or hallucinating base-paper requirements.

## How to Install and Use

You do not need to download this repository physically. You can plug it straight into your AI client using `uvx` directly from GitHub.

### For Antigravity, Cursor, or Claude Desktop
1. Open your AI agent's **MCP Settings** or `mcp.json` file.
2. Add a new server with the following JSON configuration:

```json
{
  "mcpServers": {
    "research-validator": {
      "command": "uvx",
      "args": ["git+https://github.com/YourGitHubUsername/mcp-research-validator"]
    }
  }
}
```

*(Note: Replace `YourGitHubUsername` with the actual GitHub username where this repo is hosted).*

3. Restart your AI client.

Once connected, your AI agent will automatically inherit the `self_validating_framework` rules and mathematically validate its own outputs for your research projects.

## Provided Resources & Prompts
- `self_validating_framework`: The overarching 3-Layer Validation logical rules.
- `academic_formatting_rules`: Strict IEEE formatting structural rules for LaTeX abstract and algorithmic citations.
