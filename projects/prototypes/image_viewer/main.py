import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageViewer(tk.Frame):
    """
    A simple image viewer application.
    Allows users to browse and display images using PIL (Pillow) and Tkinter.
    """
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Tkinter Image Viewer")
        self.pack(padx=20, pady=20)
        self.create_widgets()

    def create_widgets(self):
        """
        Sets up the application layout including buttons and the image display area.
        """
        # Button to open a file dialog for image selection
        self.load_button = tk.Button(self)
        self.load_button["text"] = "Load Image"
        self.load_button["command"] = self.load_image
        self.load_button.pack(side="top", pady=10)

        # Button to quit the application
        self.quit_button = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit_button.pack(side="bottom", pady=10)

        # Label used to display the loaded image
        self.image_label = tk.Label(self)
        self.image_label.pack(side="bottom", expand=True)

    def load_image(self):
        """
        Prompts the user to select an image file, then opens and displays it.
        """
        # Open a file selection dialog
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif *.bmp"), ("All files", "*.*")]
        )
        if file_path:
            try:
                # Open the image file using Pillow
                image = Image.open(file_path)
                
                # Convert the Pillow image to a Tkinter-compatible photo image
                photo = ImageTk.PhotoImage(image)
                
                # Update the label with the new image
                self.image_label.config(image=photo)
                
                # Keep a reference to avoid garbage collection of the image
                self.image_label.image = photo
            except Exception as e:
                print(f"Error loading image: {e}")

def main():
    """
    Entry point for the Image Viewer application.
    """
    root = tk.Tk()
    root.geometry("600x600")
    app = ImageViewer(master=root)
    app.mainloop()

if __name__ == "__main__":
    main()