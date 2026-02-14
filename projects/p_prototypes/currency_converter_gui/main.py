import sys
import requests
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, 
                             QLineEdit, QComboBox, QPushButton)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

class CurrencyConverter(QWidget):
    """
    A simple PySide6-based GUI for currency conversion using an external API.
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Currency Converter")
        self.resize(350, 450)
        self.init_ui()
        self.apply_styles()
        self.get_currencies()

    def init_ui(self):
        """
        Initializes and places the UI components in the window.
        """
        layout = QVBoxLayout()
        layout.setSpacing(15)
        layout.setContentsMargins(20, 20, 20, 20)

        # Amount Input
        self.amount_label = QLabel("Amount:")
        layout.addWidget(self.amount_label)
        
        self.amount_entry = QLineEdit()
        self.amount_entry.setPlaceholderText("e.g., 100.00")
        layout.addWidget(self.amount_entry)

        # 'From' Currency Selection
        self.from_currency_label = QLabel("From:")
        layout.addWidget(self.from_currency_label)
        
        self.from_currency_combo = QComboBox()
        layout.addWidget(self.from_currency_combo)

        # 'To' Currency Selection
        self.to_currency_label = QLabel("To:")
        layout.addWidget(self.to_currency_label)
        
        self.to_currency_combo = QComboBox()
        layout.addWidget(self.to_currency_combo)

        # Convert Action Button
        self.convert_button = QPushButton("Convert")
        self.convert_button.clicked.connect(self.convert)
        layout.addWidget(self.convert_button)

        # Result Display Area
        self.result_label = QLabel("")
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setFont(QFont("Helvetica", 12, QFont.Bold))
        self.result_label.setWordWrap(True)
        layout.addWidget(self.result_label)

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
            QLabel {
                font-size: 14px;
            }
            QLineEdit, QComboBox {
                background-color: #3e3e3e;
                border: 1px solid #4e4e4e;
                padding: 8px;
                border-radius: 4px;
                color: #ffffff;
            }
            QComboBox::drop-down {
                border: 0px;
            }
            QComboBox QAbstractItemView {
                background-color: #3e3e3e;
                selection-background-color: #5e5e5e;
                color: #ffffff;
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
            QPushButton:pressed {
                background-color: #3e3e3e;
            }
        """)

    def get_currencies(self):
        """
        Fetches the list of available currencies from the API to populate the comboboxes.
        """
        try:
            # Using USD as a base to get all supported currency codes
            response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
            response.raise_for_status()
            data = response.json()
            currency_list = sorted(list(data["rates"].keys()))
            
            # Populate dropdown menus
            self.from_currency_combo.addItems(currency_list)
            self.to_currency_combo.addItems(currency_list)
            
            # Set default selections
            self.from_currency_combo.setCurrentText("USD")
            self.to_currency_combo.setCurrentText("EUR")
        except requests.exceptions.RequestException as e:
            self.result_label.setText(f"Failed to load currencies: {e}")
            self.result_label.setStyleSheet("color: #ff5555;")

    def convert(self):
        """
        Performs the currency conversion based on user input and API data.
        """
        try:
            # Retrieve user input
            amount_text = self.amount_entry.text()
            if not amount_text:
                return
            amount = float(amount_text)
            from_currency = self.from_currency_combo.currentText()
            to_currency = self.to_currency_combo.currentText()

            # Fetch latest rates for the selected 'from' currency
            url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            
            # Calculate the converted amount
            conversion_rate = data["rates"][to_currency]
            converted_amount = amount * conversion_rate

            # Update the UI with the result
            self.result_label.setText(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
            self.result_label.setStyleSheet("color: #ffffff; font-weight: bold;")

        except ValueError:
            self.result_label.setText("Error: Invalid amount")
            self.result_label.setStyleSheet("color: #ff5555;")
        except requests.exceptions.RequestException as e:
            self.result_label.setText(f"Conversion error: {e}")
            self.result_label.setStyleSheet("color: #ff5555;")

def main():
    """
    Main entry point for the application.
    """
    app = QApplication(sys.argv)
    window = CurrencyConverter()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
