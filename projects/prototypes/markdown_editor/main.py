import tkinter as tk
from tkinter import filedialog
import markdown2

class MarkdownEditor(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.text = tk.Text(self)
        self.text.pack(side="left", fill="both", expand=True)

        self.html_view = tk.Text(self, state="disabled")
        self.html_view.pack(side="right", fill="both", expand=True)

        self.text.bind("<<Modified>>", self.on_text_change)

        self.save_button = tk.Button(self, text="Save", command=self.save_file)
        self.save_button.pack(side="bottom")

    def on_text_change(self, event):
        markdown_text = self.text.get("1.0", "end-1c")
        html = markdown2.markdown(markdown_text)
        self.html_view.config(state="normal")
        self.html_view.delete("1.0", "end")
        self.html_view.insert("1.0", html)
        self.html_view.config(state="disabled")

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".md")
        if file_path:
            with open(file_path, "w") as f:
                f.write(self.text.get("1.0", "end-1c"))

def main():
    root = tk.Tk()
    app = MarkdownEditor(master=root)
    app.mainloop()

if __name__ == "__main__":
    main()
