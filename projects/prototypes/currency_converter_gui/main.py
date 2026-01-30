import tkinter as tk
from tkinter import ttk
import requests

class CurrencyConverter(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.get_currencies()

    def create_widgets(self):
        self.amount_label = tk.Label(self, text="Amount:")
        self.amount_label.pack()
        self.amount_entry = tk.Entry(self)
        self.amount_entry.pack()

        self.from_currency_label = tk.Label(self, text="From:")
        self.from_currency_label.pack()
        self.from_currency_combo = ttk.Combobox(self)
        self.from_currency_combo.pack()

        self.to_currency_label = tk.Label(self, text="To:")
        self.to_currency_label.pack()
        self.to_currency_combo = ttk.Combobox(self)
        self.to_currency_combo.pack()

        self.convert_button = tk.Button(self, text="Convert", command=self.convert)
        self.convert_button.pack()

        self.result_label = tk.Label(self, text="")
        self.result_label.pack()

    def get_currencies(self):
        try:
            response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
            response.raise_for_status()
            data = response.json()
            self.from_currency_combo["values"] = list(data["rates"].keys())
            self.to_currency_combo["values"] = list(data["rates"].keys())
        except requests.exceptions.RequestException as e:
            self.result_label.config(text=f"Error: {e}")

    def convert(self):
        try:
            amount = float(self.amount_entry.get())
            from_currency = self.from_currency_combo.get()
            to_currency = self.to_currency_combo.get()

            url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            
            conversion_rate = data["rates"][to_currency]
            converted_amount = amount * conversion_rate

            self.result_label.config(text=f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")

        except ValueError:
            self.result_label.config(text="Error: Invalid amount")
        except requests.exceptions.RequestException as e:
            self.result_label.config(text=f"Error: {e}")

def main():
    root = tk.Tk()
    app = CurrencyConverter(master=root)
    app.mainloop()

if __name__ == "__main__":
    main()
