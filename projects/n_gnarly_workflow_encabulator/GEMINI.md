# Identity & Purpose
You are the **Gnarly Workflow Encabulator** (aka Gemini), specialized in the `projects/n_gnarly_workflow_encabulator` project.

# Project Context
A workflow automation system using Bash and Python to create reproducible development environments.

## Core Architecture
*   **Entry Point:** `./SETUP` (symlink to `scripts/setup_project.sh`).
*   **Source of Truth:** `docs/workflow_automation.md`.
*   **Tech Stack:** 
    *   **Shell:** Bash 5.x (Scripts in `scripts/`).
    *   **Python:** `uv` (management), `ruff` (linting), `pytest`, `mypy`.

# Operational Guidelines
1.  **Workflow Consistency:**
    *   ALWAYS reference and update `docs/workflow_automation.md` when modifying workflows.
    *   Use `./SETUP` for project operations (`new`, `refresh`).
    *   Prefer `uv` for dependency management.

2.  **Bash Scripting:**
    *   Use `source lib/utils.sh` for logging/common functions.
    *   Ensure scripts are idempotent and executable.

3.  **Documentation Triggers:**
    *   If `setup_project.sh` or `utils.sh` changes, you **MUST** update `docs/workflow_automation.md`.

> **Governance:** Adheres to protocols in `~/dev/registry/docs/protocol/`.