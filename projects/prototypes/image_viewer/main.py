import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageViewer(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.load_button = tk.Button(self)
        self.load_button["text"] = "Load Image"
        self.load_button["command"] = self.load_image
        self.load_button.pack(side="top")

        self.quit_button = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit_button.pack(side="bottom")

        self.image_label = tk.Label(self)
        self.image_label.pack(side="bottom")

    def load_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            image = Image.open(file_path)
            photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=photo)
            self.image_label.image = photo

def main():
    root = tk.Tk()
    app = ImageViewer(master=root)
    app.mainloop()

if __name__ == "__main__":
    main()
