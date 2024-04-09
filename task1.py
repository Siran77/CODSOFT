import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3

class ToDoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List")
        self.db_connection = sqlite3.connect("todo.db")
        self.create_table_if_not_exists()
        self.create_widgets()
        self.populate_list()

    def create_table_if_not_exists(self):
        cursor = self.db_connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY,
                description TEXT,
                completed BOOLEAN
            )
        """)
        self.db_connection.commit()

    def create_widgets(self):
        self.task_entry = ttk.Entry(self.master, width=40)
        self.task_entry.grid(row=0, column=0, padx=5, pady=5)

        self.add_button = ttk.Button(self.master, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=5, pady=5)

        self.task_list = tk.Listbox(self.master, height=15, width=50)
        self.task_list.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        self.complete_button = ttk.Button(self.master, text="Mark Complete", command=self.mark_complete)
        self.complete_button.grid(row=2, column=0, padx=5, pady=5)

        self.delete_button = ttk.Button(self.master, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=2, column=1, padx=5, pady=5)

        self.style = ttk.Style()
        self.style.configure("Listbox", background="#f0f0f0", foreground="black", font=("Helvetica", 10))

    def populate_list(self):
        self.task_list.delete(0, tk.END)
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT * FROM tasks")
        tasks = cursor.fetchall()
        for task in tasks:
            self.task_list.insert(tk.END, f"{task[1]} {'(Completed)' if task[2] else ''}")

    def add_task(self):
        task_description = self.task_entry.get()
        if task_description:
            cursor = self.db_connection.cursor()
            cursor.execute("INSERT INTO tasks (description, completed) VALUES (?, ?)", (task_description, False))
            self.db_connection.commit()
            self.task_entry.delete(0, tk.END)
            self.populate_list()

    def mark_complete(self):
        try:
            index = self.task_list.curselection()[0]
            cursor = self.db_connection.cursor()
            cursor.execute("UPDATE tasks SET completed = ? WHERE id = ?", (True, index+1))
            self.db_connection.commit()
            self.populate_list()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task.")

    def delete_task(self):
        try:
            index = self.task_list.curselection()[0]
            cursor = self.db_connection.cursor()
            cursor.execute("DELETE FROM tasks WHERE id = ?", (index+1,))
            self.db_connection.commit()
            self.populate_list()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task.")

def main():
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
