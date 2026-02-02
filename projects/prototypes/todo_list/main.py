import tkinter as tk

class TodoList(tk.Frame):
    """
    A basic To-Do List application built with Tkinter.
    Allows users to add and delete tasks from a list.
    """
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Tkinter To-Do List")
        self.pack(padx=10, pady=10)
        self.create_widgets()
        # Internal list to store task strings
        self.tasks = []

    def create_widgets(self):
        """
        Sets up the input field, buttons, and listbox for the application.
        """
        # Entry field for typing new tasks
        self.task_entry = tk.Entry(self)
        self.task_entry.pack(side="top", fill="x", pady=5)

        # Button to trigger task addition
        self.add_button = tk.Button(self)
        self.add_button["text"] = "Add Task"
        self.add_button["command"] = self.add_task
        self.add_button.pack(side="top", pady=2)

        # Listbox to display current tasks
        self.task_list = tk.Listbox(self)
        self.task_list.pack(side="top", fill="both", expand=True, pady=5)

        # Button to delete the currently selected task in the listbox
        self.delete_button = tk.Button(self, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(side="bottom", pady=2)

    def add_task(self):
        """
        Retrieves the text from the entry field and adds it to the task list.
        """
        task = self.task_entry.get().strip()
        if task:
            # Append to our internal data structure
            self.tasks.append(task)
            # Refresh the visible listbox
            self.update_task_list()
            # Clear the entry field for the next task
            self.task_entry.delete(0, "end")

    def delete_task(self):
        """
        Removes the selected task from both the internal list and the display.
        """
        # Get the index of the selected item in the Listbox
        selected_task_index = self.task_list.curselection()
        if selected_task_index:
            # Remove from internal list by index
            self.tasks.pop(selected_task_index[0])
            # Refresh the visible listbox
            self.update_task_list()

    def update_task_list(self):
        """
        Clears the listbox and re-populates it with items from the tasks list.
        """
        self.task_list.delete(0, "end")
        for task in self.tasks:
            self.task_list.insert("end", task)

def main():
    """
    Initializes the Tkinter root window and runs the application loop.
    """
    root = tk.Tk()
    app = TodoList(master=root)
    app.mainloop()

if __name__ == "__main__":
    main()