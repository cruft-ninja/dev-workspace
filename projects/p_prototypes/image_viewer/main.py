import sys
import os
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, 
                             QPushButton, QFileDialog, QScrollArea)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap

class ImageViewer(QWidget):
    """
    A simple image viewer application built with PySide6.
    Allows users to browse and display images.
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PySide6 Image Viewer")
        self.resize(800, 600)
        self.init_ui()
        self.apply_styles()

    def init_ui(self):
        """
        Sets up the application layout including buttons and the image display area.
        """
        layout = QVBoxLayout()

        # Button to open a file dialog for image selection
        self.load_button = QPushButton("Load Image")
        self.load_button.clicked.connect(self.load_image)
        layout.addWidget(self.load_button)

        # Scroll Area to handle large images
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setAlignment(Qt.AlignCenter)
        
        # Label used to display the loaded image
        self.image_label = QLabel("No Image Loaded")
        self.image_label.setAlignment(Qt.AlignCenter)
        self.scroll_area.setWidget(self.image_label)
        
        layout.addWidget(self.scroll_area)

        # Button to quit the application
        self.quit_button = QPushButton("QUIT")
        self.quit_button.clicked.connect(self.close)
        layout.addWidget(self.quit_button)

        self.setLayout(layout)

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
            QPushButton {
                background-color: #4e4e4e;
                border: 1px solid #5e5e5e;
                padding: 10px;
                border-radius: 4px;
                color: #ffffff;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #5e5e5e;
            }
            QScrollArea {
                border: 1px solid #4e4e4e;
                background-color: #1e1e1e;
            }
            QLabel {
                color: #888888;
                font-size: 16px;
            }
        """)

    def load_image(self):
        """
        Prompts the user to select an image file, then opens and displays it.
        """
        file_path, _ = QFileDialog.getOpenFileName(
            self, 
            "Open Image", 
            "", 
            "Image files (*.jpg *.jpeg *.png *.gif *.bmp);;All files (*)"
        )
        
        if file_path:
            pixmap = QPixmap(file_path)
            if not pixmap.isNull():
                self.image_label.setPixmap(pixmap)
                self.image_label.setText("") # Clear "No Image Loaded" text
                self.setWindowTitle(f"PySide6 Image Viewer - {os.path.basename(file_path)}")
            else:
                self.image_label.setText("Error loading image")

def main():
    """
    Entry point for the Image Viewer application.
    """
    app = QApplication(sys.argv)
    window = ImageViewer()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
