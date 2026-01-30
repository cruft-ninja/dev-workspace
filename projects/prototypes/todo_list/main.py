import tkinter as tk

class TodoList(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.tasks = []

    def create_widgets(self):
        self.task_entry = tk.Entry(self)
        self.task_entry.pack(side="top", fill="x")

        self.add_button = tk.Button(self)
        self.add_button["text"] = "Add Task"
        self.add_button["command"] = self.add_task
        self.add_button.pack(side="top")

        self.task_list = tk.Listbox(self)
        self.task_list.pack(side="top", fill="both", expand=True)

        self.delete_button = tk.Button(self, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(side="bottom")

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_list()
            self.task_entry.delete(0, "end")

    def delete_task(self):
        selected_task_index = self.task_list.curselection()
        if selected_task_index:
            self.tasks.pop(selected_task_index[0])
            self.update_task_list()

    def update_task_list(self):
        self.task_list.delete(0, "end")
        for task in self.tasks:
            self.task_list.insert("end", task)

def main():
    root = tk.Tk()
    app = TodoList(master=root)
    app.mainloop()

if __name__ == "__main__":
    main()
