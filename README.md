# Dev Workspace Monorepo

This is the central repository for my personal development projects, automation tools, and documentation. It consolidates multiple previous repositories into a single, unified codebase.

## 📂 Project Directory

### 💻 Development
*   **[Prototypes](projects/prototypes/README.md)**  
    Rapid prototyping of new ideas.
*   **[Reference Materials](projects/reference_materials/README.md)**  
    A collection of useful documents, articles, and code snippets.

### 📊 Data
*   **[Data Analysis](projects/data_analysis/README.md)**  
    Data analysis projects.

### 🛠️ Tools & Automation
*   **[Gnarly Workflow Encabulator (CLI Bootstrap)](projects/cli_bootstrap_tools/README.md)**  
    A CLI automation tool for bootstrapping reproducible Python environments using `uv`, `ruff`, and `git`.
*   **[Script Runner GUI](projects/task_runner_gui/README.md)**  
    A modern Tkinter/Python GUI for organizing and executing bash scripts with a "Command Center" interface.

### 📚 Documentation & Knowledge
*   **[Prompt Engineering Spoke](projects/prompt_engineering/README.md)**  
    The unified hub for the **Library** (Best Practices) and the **Workshop** (Mentorship & Logs).
*   **[Gemini Internals](projects/docs_gemini_internals/README.md)**  
    Deep-dive documentation on the CLI ecosystem and LLM interactions.

## 🛡️ Security & Governance

This workspace operates under a strict **Defense-in-Depth** security model.

*   **Policy:** All agents must adhere to [AI_SECURITY_POLICY.md](registry/docs/protocol/AI_SECURITY_POLICY.md).
*   **Standards:** Documentation standards are defined in [AI_DOCS_STANDARD.md](registry/docs/protocol/AI_DOCS_STANDARD.md).
*   **Sandboxing:** Dangerous or complex tasks are executed within a confined environment.

## 🚀 Quick Start

1.  **Explore:** Browse the `projects/` directory to find specific tools.
2.  **Run:** Most tools have their own `README.md` with specific installation and usage instructions.

## 🤖 Script Manager

This repository includes a `manager` script that provides quick access to common system administration tasks. The script is POSIX compliant.

**Usage:**

```bash
./manager [command]
```

**Available Commands:**

*   `users`: List logged-in users.
*   `disk`: Show disk usage.
*   `mem`: Show memory usage.
*   `ps`: Show running processes.
*   `net`: Show network status.
