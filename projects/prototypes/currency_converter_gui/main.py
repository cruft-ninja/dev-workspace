import tkinter as tk
from tkinter import ttk
import requests

class CurrencyConverter(tk.Frame):
    """
    A simple Tkinter-based GUI for currency conversion using an external API.
    """
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Currency Converter")
        self.pack(padx=20, pady=20)
        self.create_widgets()
        self.get_currencies()

    def create_widgets(self):
        """
        Initializes and places the UI components in the window.
        """
        # Amount Input
        self.amount_label = tk.Label(self, text="Amount:")
        self.amount_label.pack()
        self.amount_entry = tk.Entry(self)
        self.amount_entry.pack(pady=5)

        # 'From' Currency Selection
        self.from_currency_label = tk.Label(self, text="From:")
        self.from_currency_label.pack()
        self.from_currency_combo = ttk.Combobox(self, state="readonly")
        self.from_currency_combo.pack(pady=5)

        # 'To' Currency Selection
        self.to_currency_label = tk.Label(self, text="To:")
        self.to_currency_label.pack()
        self.to_currency_combo = ttk.Combobox(self, state="readonly")
        self.to_currency_combo.pack(pady=5)

        # Convert Action Button
        self.convert_button = tk.Button(self, text="Convert", command=self.convert)
        self.convert_button.pack(pady=10)

        # Result Display Area
        self.result_label = tk.Label(self, text="", font=("Helvetica", 12, "bold"))
        self.result_label.pack()

    def get_currencies(self):
        """
        Fetches the list of available currencies from the API to populate the comboboxes.
        """
        try:
            # Using USD as a base to get all supported currency codes
            response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
            response.raise_for_status()
            data = response.json()
            currency_list = list(data["rates"].keys())
            
            # Populate dropdown menus
            self.from_currency_combo["values"] = currency_list
            self.to_currency_combo["values"] = currency_list
            
            # Set default selections
            self.from_currency_combo.set("USD")
            self.to_currency_combo.set("EUR")
        except requests.exceptions.RequestException as e:
            self.result_label.config(text=f"Failed to load currencies: {e}", fg="red")

    def convert(self):
        """
        Performs the currency conversion based on user input and API data.
        """
        try:
            # Retrieve user input
            amount = float(self.amount_entry.get())
            from_currency = self.from_currency_combo.get()
            to_currency = self.to_currency_combo.get()

            # Fetch latest rates for the selected 'from' currency
            url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            
            # Calculate the converted amount
            conversion_rate = data["rates"][to_currency]
            converted_amount = amount * conversion_rate

            # Update the UI with the result
            self.result_label.config(text=f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}", fg="black")

        except ValueError:
            # Handle non-numeric input for amount
            self.result_label.config(text="Error: Invalid amount", fg="red")
        except requests.exceptions.RequestException as e:
            # Handle API/Network errors during conversion
            self.result_label.config(text=f"Conversion error: {e}", fg="red")

def main():
    """
    Main entry point for the application.
    """
    root = tk.Tk()
    app = CurrencyConverter(master=root)
    app.mainloop()

if __name__ == "__main__":
    main()