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
      "args": ["git+https://github.com/Aldrin-56/mcp-research-validator"]
    }
  }
}
```

3. Restart your AI client.

## User Manual: How to use it in Chat

Once installed, you don't need to write any code. Just talk to your AI naturally. 

**Example Workflow:**
1. Open a new chat in Cursor/Claude/Antigravity.
2. Ask the AI: *"I need to write the simulation section. Please use the `self_validating_framework` prompt from your MCP tools to ensure you don't hallucinate."*
3. The AI will automatically fetch the rules from this server, lock onto the exact algorithm names from your base paper, and only write the code after mathematically proving that it hasn't deviated from your project's scope. 

If the AI senses it is missing context, the framework forces it to **STOP** and ask you for the ground-truth data instead of guessing.

Once connected, your AI agent will automatically inherit the `self_validating_framework` rules and mathematically validate its own outputs for your research projects.

## Provided Resources & Prompts
- `self_validating_framework`: The overarching 3-Layer Validation logical rules.
- `academic_formatting_rules`: Strict IEEE formatting structural rules for LaTeX abstract and algorithmic citations.
