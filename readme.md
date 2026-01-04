# Gnarly Workflow Encabulator

A CLI automation tool for bootstrapping reproducible Python environments. Orchestrates Git, uv, Ruff, and GitHub Actions for instant project setup.

## Quick Start

### 1. Load Shortcuts

```bash
source bash/aliases.sh
```

### 2. Run the Master Setup

Launch the interactive menu to manage your projects:

```bash
./SETUP
```

### 3. Maintenance

If you move or rename the folder, refresh your environments:

```bash
./SETUP refresh
```

## Documentation & Cheatsheets

We have prepared quick reference guides for the tools used in this project:

- [Git Basics](docs/cheatsheets/git.md)
- [Bash Commands](docs/cheatsheets/bash.md)
- [Python Basics](docs/cheatsheets/python.md)
- [uv (Package Manager)](docs/cheatsheets/uv.md)
- [Ruff (Linter/Formatter)](docs/cheatsheets/ruff.md)
- [Pytest (Testing)](docs/cheatsheets/pytest.md)
- [Make (Automation)](docs/cheatsheets/make.md)
- [Markdown Syntax](docs/cheatsheets/markdown.md)
- [Nano Editor](docs/cheatsheets/nano.md)

## Security & Governance

This workspace operates under a **Defense-in-Depth** security model.
*   **Policy Source:** `~/dev/AI_SECURITY_POLICY.md`
*   **Enforcement:**
    *   **Direct:** Agents must adhere to the policy rules.
    *   **Physical:** Sub-projects should be accessed via `gemini-safe` to enforce directory confinement.
*   **Your Role:** As the root agent, you are the **Security Architect**. You are responsible for maintaining the policy, ensuring `gemini-safe` functionality, and auditing sub-agents if requested.

---
# GLOBAL SECURITY CONTEXT
> **IMPORTANT:** You are strictly bound by the security and operational rules defined in `~/dev/AI_SECURITY_POLICY.md`. You must read and adhere to these rules at all times.
