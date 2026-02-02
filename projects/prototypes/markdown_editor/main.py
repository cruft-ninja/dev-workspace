import tkinter as tk
from tkinter import filedialog
import markdown2

class MarkdownEditor(tk.Frame):
    """
    A simple Markdown editor with live HTML preview.
    Uses 'markdown2' for conversion and 'Tkinter' for the GUI.
    """
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Markdown Editor & Preview")
        self.pack(fill="both", expand=True)
        self.create_widgets()

    def create_widgets(self):
        """
        Initializes the layout with an editor pane and a preview pane.
        """
        # Left pane: Markdown input
        self.text = tk.Text(self, undo=True)
        self.text.pack(side="left", fill="both", expand=True, padx=5, pady=5)

        # Right pane: HTML output (preview)
        self.html_view = tk.Text(self, state="disabled", bg="#f0f0f0")
        self.html_view.pack(side="right", fill="both", expand=True, padx=5, pady=5)

        # Bind text modification event to trigger the live preview update
        self.text.bind("<<Modified>>", self.on_text_change)

        # Save button at the bottom
        self.save_button = tk.Button(self, text="Save Markdown File", command=self.save_file)
        self.save_button.pack(side="bottom", pady=5)

    def on_text_change(self, event):
        """
        Called whenever the text in the editor changes.
        Converts Markdown to HTML and updates the preview pane.
        """
        # Get raw text from the editor
        markdown_text = self.text.get("1.0", "end-1c")
        
        # Convert Markdown string to HTML string
        html = markdown2.markdown(markdown_text)
        
        # Update the preview (must temporarily enable state to modify content)
        self.html_view.config(state="normal")
        self.html_view.delete("1.0", "end")
        self.html_view.insert("1.0", html)
        self.html_view.config(state="disabled")
        
        # Reset the modified flag so future changes trigger the event again
        self.text.edit_modified(False)

    def save_file(self):
        """
        Opens a save dialog and writes the editor content to a file.
        """
        file_path = filedialog.asksaveasfilename(
            defaultextension=".md",
            filetypes=[("Markdown files", "*.md"), ("All files", "*.*")]
        )
        if file_path:
            try:
                with open(file_path, "w") as f:
                    f.write(self.text.get("1.0", "end-1c"))
                print(f"File saved to: {file_path}")
            except Exception as e:
                print(f"Error saving file: {e}")

def main():
    """
    Sets up the Tkinter application.
    """
    root = tk.Tk()
    root.geometry("800x600")
    app = MarkdownEditor(master=root)
    app.mainloop()

if __name__ == "__main__":
    main()