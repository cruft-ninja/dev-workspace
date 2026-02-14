import sys
import os
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
                             QPlainTextEdit, QTextBrowser, QPushButton, QFileDialog)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
import markdown2

class MarkdownEditor(QWidget):
    """
    A simple Markdown editor with live HTML preview.
    Uses 'markdown2' for conversion and 'PySide6' for the GUI.
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Markdown Editor & Preview")
        self.resize(1000, 700)
        self.init_ui()
        self.apply_styles()

    def init_ui(self):
        """
        Initializes the layout with an editor pane and a preview pane.
        """
        main_layout = QVBoxLayout()
        
        # Splitter-like layout for editor and preview
        panes_layout = QHBoxLayout()
        
        # Left pane: Markdown input
        self.editor = QPlainTextEdit()
        self.editor.setPlaceholderText("Type your Markdown here...")
        self.editor.textChanged.connect(self.update_preview)
        panes_layout.addWidget(self.editor)

        # Right pane: HTML output (preview)
        self.preview = QTextBrowser()
        self.preview.setOpenExternalLinks(True)
        panes_layout.addWidget(self.preview)
        
        main_layout.addLayout(panes_layout)

        # Save button
        self.save_button = QPushButton("Save Markdown File")
        self.save_button.clicked.connect(self.save_file)
        main_layout.addWidget(self.save_button)

        self.setLayout(main_layout)

    def apply_styles(self):
        """
        Applies a dark theme using Qt Style Sheets.
        """
        self.setStyleSheet("""
            QWidget {
                background-color: #2e2e2e;
                color: #d4d4d4;
                font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
            }
            QPlainTextEdit {
                background-color: #1e1e1e;
                border: 1px solid #333333;
                padding: 10px;
                font-size: 14px;
                color: #d4d4d4;
            }
            QTextBrowser {
                background-color: #252526;
                border: 1px solid #333333;
                padding: 10px;
                font-size: 14px;
                color: #e0e0e0;
            }
            QPushButton {
                background-color: #4e4e4e;
                border: 1px solid #5e5e5e;
                padding: 8px;
                border-radius: 4px;
                color: #ffffff;
                font-family: "Segoe UI", sans-serif;
                font-size: 13px;
            }
            QPushButton:hover {
                background-color: #5e5e5e;
            }
        """)

    def update_preview(self):
        """
        Called whenever the text in the editor changes.
        Converts Markdown to HTML and updates the preview pane.
        """
        markdown_text = self.editor.toPlainText()
        html = markdown2.markdown(markdown_text)
        
        # Add some basic CSS for the preview to look better in dark mode
        styled_html = f"""
        <style>
            body {{ font-family: sans-serif; color: #e0e0e0; line-height: 1.6; }}
            code {{ background-color: #333333; padding: 2px 4px; border-radius: 4px; }}
            pre {{ background-color: #333333; padding: 10px; border-radius: 4px; overflow-x: auto; }}
            blockquote {{ border-left: 4px solid #5e5e5e; padding-left: 10px; color: #a0a0a0; }}
            a {{ color: #4fc3f7; }}
        </style>
        {html}
        """
        self.preview.setHtml(styled_html)

    def save_file(self):
        """
        Opens a save dialog and writes the editor content to a file.
        """
        file_path, _ = QFileDialog.getSaveFileName(
            self, 
            "Save Markdown", 
            "", 
            "Markdown Files (*.md);;All Files (*)"
        )
        
        if file_path:
            try:
                with open(file_path, "w") as f:
                    f.write(self.editor.toPlainText())
            except Exception as e:
                print(f"Error saving file: {e}")

def main():
    """
    Sets up the PySide6 application.
    """
    app = QApplication(sys.argv)
    window = MarkdownEditor()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
