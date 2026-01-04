# Dev Workspace Monorepo

This is the central repository for my personal development projects, automation tools, and documentation. It consolidates multiple previous repositories into a single, unified codebase.

## 📂 Project Directory

### 🛠️ Tools & Automation
*   **[Gnarly Workflow Encabulator](./gnarly_workflow_encabulator/README.md)**  
    A CLI automation tool for bootstrapping reproducible Python environments using `uv`, `ruff`, and `git`.
*   **[Script Runner](./script_runner/README.md)**  
    A modern Tkinter/Python GUI for organizing and executing bash scripts with a "Command Center" interface.

### 📚 Documentation & Guides
*   **[Prompt Engineering Best Practices](./prompt_engineering_best_practices/README.md)**  
    A collection of guides, templates, and resources for mastering LLM prompting.
*   **[AI Gemini Guru](./ai_gemini_guru/)**  
    Internal documentation regarding the architecture, memory, and operational logic of this Gemini CLI agent.
*   **[AI Prompt Mentor](./ai_prompt_mentor/)**  
    Session logs and notes from interactive prompting mentorship sessions.

## 🛡️ Security & Governance

This workspace operates under a strict **Defense-in-Depth** security model.

*   **Policy:** All agents must adhere to [AI_SECURITY_POLICY.md](./AI_SECURITY_POLICY.md).
*   **Sandboxing:** Dangerous or complex tasks are executed within a confined environment using the `gemini-safe` wrapper.

## 🚀 Quick Start

1.  **Explore:** Browse the sub-directories to find specific tools.
2.  **Run:** Most tools have their own `README.md` with specific installation and usage instructions.