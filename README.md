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

## 🤖 System Administration Scripts

This repository includes a collection of utility scripts in the `utils/` directory for common system administration tasks.

**Usage:**

```bash
./utils/<script_name>.sh
```

**Available Utilities:**

*   **`user_list.sh`**: List logged-in human users.
*   **`disk_monitor.sh`**: Show disk usage for the root filesystem.
*   **`mem_hogs.sh`**: Show top processes by memory usage.
*   **`check_cpu.sh`**: Check current CPU load.
*   **`port_listen.sh`**: Show active network listeners.
*   **`sys_info.sh`**: Show general system health summary.
