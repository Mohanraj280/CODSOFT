import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Creative To-Do List")

        self.tasks = []

        # Entry for adding tasks
        self.task_entry = tk.Entry(root, width=40, font=("Arial", 12))
        self.task_entry.pack(pady=10)

        # Add task button
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task, font=("Arial", 12))
        self.add_button.pack()

        # Task listbox with a scrollbar
        self.task_listbox = tk.Listbox(root, width=40, height=10, selectbackground="lightblue", selectmode=tk.SINGLE, font=("Arial", 12))
        self.task_listbox.pack()

        # Scrollbar for the listbox
        self.scrollbar = tk.Scrollbar(root)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        # Complete and Remove buttons
        self.complete_button = tk.Button(root, text="Mark Complete", command=self.mark_complete, font=("Arial", 12))
        self.complete_button.pack()

        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task, font=("Arial", 12))
        self.remove_button.pack()

        # Update the listbox
        self.update_listbox()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_entry.delete(0, tk.END)
            self.update_listbox()

    def mark_complete(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_index = selected_index[0]
            self.tasks[task_index] = "[DONE] " + self.tasks[task_index]
            self.update_listbox()

    def remove_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_index = selected_index[0]
            del self.tasks[task_index]
            self.update_listbox()

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
