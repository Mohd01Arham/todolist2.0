import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x400")
        
        # Task entry field
        self.task_var = tk.StringVar()
        tk.Entry(self.root, textvariable=self.task_var, width=30).pack(pady=10)
        
        # Add task button
        tk.Button(self.root, text="Add Task", command=self.add_task).pack(pady=5)
        
        # Task list display
        self.task_listbox = tk.Listbox(self.root, selectmode=tk.MULTIPLE, width=30, height=10)
        self.task_listbox.pack(pady=10)
        
        # Mark as complete button
        tk.Button(self.root, text="Mark as Complete", command=self.mark_complete).pack(pady=5)
        
        # Delete selected task button
        tk.Button(self.root, text="Delete Selected", command=self.delete_task).pack(pady=5)
        
        # Task list
        self.tasks = []

    def add_task(self):
        task = self.task_var.get()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.update_task_listbox()
            self.task_var.set("")
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")
    
    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            display_text = f"{'[X]' if task['completed'] else '[ ]'} {task['task']}"
            self.task_listbox.insert(tk.END, display_text)
    
    def mark_complete(self):
        selected_indices = self.task_listbox.curselection()
        for i in selected_indices:
            self.tasks[i]["completed"] = True
        self.update_task_listbox()
    
    def delete_task(self):
        selected_indices = list(self.task_listbox.curselection())
        for i in reversed(selected_indices):
            del self.tasks[i]
        self.update_task_listbox()

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
