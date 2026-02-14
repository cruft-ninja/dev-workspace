import sys
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, 
                             QLineEdit, QPushButton, QListWidget)
from PySide6.QtCore import Qt

class TodoList(QWidget):
    """
    A basic To-Do List application built with PySide6.
    Allows users to add and delete tasks from a list.
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PySide6 To-Do List")
        self.resize(300, 400)
        self.tasks = []
        self.init_ui()
        self.apply_styles()

    def init_ui(self):
        """
        Sets up the input field, buttons, and list widget for the application.
        """
        self.layout = QVBoxLayout()

        # Entry field for typing new tasks
        self.task_entry = QLineEdit()
        self.task_entry.setPlaceholderText("Enter a task...")
        self.task_entry.returnPressed.connect(self.add_task)
        self.layout.addWidget(self.task_entry)

        # Button to trigger task addition
        self.add_button = QPushButton("Add Task")
        self.add_button.clicked.connect(self.add_task)
        self.layout.addWidget(self.add_button)

        # List widget to display current tasks
        self.task_list = QListWidget()
        self.layout.addWidget(self.task_list)

        # Button to delete the currently selected task
        self.delete_button = QPushButton("Delete Task")
        self.delete_button.clicked.connect(self.delete_task)
        self.layout.addWidget(self.delete_button)

        self.setLayout(self.layout)

    def apply_styles(self):
        """
        Applies a dark theme using Qt Style Sheets.
        """
        self.setStyleSheet("""
            QWidget {
                background-color: #2e2e2e;
                color: #ffffff;
                font-family: "Segoe UI", sans-serif;
            }
            QLineEdit {
                background-color: #3e3e3e;
                border: 1px solid #4e4e4e;
                padding: 8px;
                border-radius: 4px;
                color: #ffffff;
            }
            QPushButton {
                background-color: #4e4e4e;
                border: 1px solid #5e5e5e;
                padding: 8px;
                border-radius: 4px;
                color: #ffffff;
            }
            QPushButton:hover {
                background-color: #5e5e5e;
            }
            QPushButton:pressed {
                background-color: #3e3e3e;
            }
            QListWidget {
                background-color: #3e3e3e;
                border: 1px solid #4e4e4e;
                border-radius: 4px;
                color: #ffffff;
                outline: none;
            }
            QListWidget::item {
                padding: 5px;
            }
            QListWidget::item:selected {
                background-color: #5e5e5e;
                color: #ffffff;
            }
        """)

    def add_task(self):
        """
        Retrieves text from the entry and adds it to the list.
        """
        task = self.task_entry.text().strip()
        if task:
            self.tasks.append(task)
            self.task_list.addItem(task)
            self.task_entry.clear()

    def delete_task(self):
        """
        Removes the selected task from the list.
        """
        selected_items = self.task_list.selectedItems()
        if not selected_items:
            return
        for item in selected_items:
            row = self.task_list.row(item)
            self.task_list.takeItem(row)
            if 0 <= row < len(self.tasks):
                self.tasks.pop(row)

def main():
    """
    Initializes the PySide6 application and runs the event loop.
    """
    app = QApplication(sys.argv)
    todo = TodoList()
    todo.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
