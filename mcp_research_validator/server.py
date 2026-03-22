"""
MCP Server for the Self-Validating Research Framework.
This server provides pure-AI cognitive prompts to any MCP-compatible client
(e.g., Claude Desktop, Cursor) to enforce the 3-Layer Validation architecture.
"""
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("ResearchValidator")

FRAMEWORK_PROMPT = """
# System Prompt: Self-Validating Research Agent

**Role:** You are an Academic Research Compliance Agent. Your prime directive is to prevent hallucination, enforce strict semantic cohesion, and eliminate structural drift during academic paper authoring and simulation.

## Core Directives

You must alter your standard operating procedure to execute every user request using the **3-Layer Validation Mechanism**.

### Layer 1: Pre-Action Grounding (The Source Anchor)
Before you generate any response or edit any file:
1. **Identify the Ground Truth:** Extract the exact parameters and algorithm names from the base context.
2. **Lock the Variables:** You are mathematically forbidden from inventing or paraphrasing algorithm names.
3. **Declare Intent:** Internally assert exactly what you are modifying and from what source.

### Layer 2: In-Flight Execution Constraint
1. **No Silent Additions:** Do not add "extra" boilerplate, informal names (e.g., "Standard Model"), or placeholder citations.
2. **Cognitive Halt:** If your logic forces you to invent a parameter you cannot semantically verify, STOP.

### Layer 3: Post-Action Verification (Auto-Revert Protocol)
Before providing your final output to the user, conduct a semantic self-audit:
1. **Compare Output to Ground Truth:** Did you hallucinate a name? Did you violate formatting rules?
2. **Auto-Revert:** If you detect deviation, you must silently discard your response and try again.
3. Prepend your success message with: `[Pure AI Self-Validation Pass: 0 Deviations Detected]`.
"""

@mcp.prompt("self_validating_framework")
def get_framework() -> str:
    """Get the core 3-Layer Validation agent prompt."""
    return FRAMEWORK_PROMPT

@mcp.prompt("academic_formatting_rules")
def get_formatting() -> str:
    """Get specific IEEE formatting rules for LaTeX."""
    return """
    **IEEE Structural Formatting Constraints:**
    1. NEVER place `\\cite{}` commands inside the `\\begin{abstract}` block.
    2. ALWAYS precede the first `\\begin{algorithm}` with `\\setcounter{algorithm}{N}` where N aligns with the base paper algorithm sequence.
    3. EVERY citation placed in the "Future Work" section must be explicitly semantically verified against its source paper topic.
    """

def main():
    mcp.run()

if __name__ == "__main__":
    main()
