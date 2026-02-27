# PySide6 Demo

A basic prototype demonstrating a simple GUI application using PySide6 (Qt for Python).

## Overview

This project serves as a minimal template for building desktop applications with Python and Qt. It displays a window with a centered "Hello, PySide6!" label.

## Prerequisites

- Python 3.12+
- `uv` package manager (recommended)

## Setup & Run

1.  **Install dependencies:**
    ```bash
    uv sync
    ```

2.  **Run the application:**
    ```bash
    uv run main.py
    ```

## Troubleshooting

### Linux: `qt.qpa.plugin` error

If you encounter an error like:
> `qt.qpa.plugin: From 6.5.0, xcb-cursor0 or libxcb-cursor0 is needed to load the Qt xcb platform plugin.`

You need to install the missing system library:

```bash
sudo apt-get install libxcb-cursor0
```

## Project Structure

- `main.py`: The entry point containing the `QApplication` and `QMainWindow` logic.
- `pyproject.toml`: Configuration and dependencies (specifically `pyside6`).
