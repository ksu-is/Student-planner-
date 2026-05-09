import tkinter as tk
import json
import os
from tkinter import messagebox

DATA_FILE = "tasks.json"

def update_count():
    status_label.config(text=f"Total Tasks: {listbox.size()}")

def save_tasks():
    tasks = listbox.get(0, tk.END)
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f)
    update_count()

def load_tasks():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            tasks = json.load(f)
            for task in tasks:
                listbox.insert(tk.END, task)
    update_count()

def add_task():
    task = task_entry.get()
    if task:
        listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        save_tasks()

def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
        save_tasks()
    except:
        pass

def clear_all():
    if messagebox.askyesno("Confirm", "Clear all tasks?"):
        listbox.delete(0, tk.END)
        save_tasks()

def main():
    global task_entry, listbox, status_label
    root = tk.Tk()
    root.title("Student Planner App")
    root.geometry("420x600")
    
    tk.Label(root, text="My Student Planner", font=("Arial", 16, "bold")).pack(pady=10)
    task_entry = tk.Entry(root, width=35)
    task_entry.pack(pady=5)

    btn_frame = tk.Frame(root)
    btn_frame.pack(pady=10)

    tk.Button(btn_frame, text="Add Task", command=add_task, bg="green", fg="white", width=12).grid(row=0, column=0, padx=5)
    tk.Button(btn_frame, text="Delete Task", command=delete_task, bg="orange", fg="white", width=12).grid(row=0, column=1, padx=5)
    tk.Button(btn_frame, text="Clear All", command=clear_all, bg="red", fg="white", width=12).grid(row=0, column=2, padx=5)

    list_frame = tk.Frame(root)
    list_frame.pack(pady=10)

    scrollbar = tk.Scrollbar(list_frame, orient=tk.VERTICAL)
    listbox = tk.Listbox(list_frame, width=45, height=15, yscrollcommand=scrollbar.set)
    
    scrollbar.config(command=listbox.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    listbox.pack(side=tk.LEFT)

    status_label = tk.Label(root, text="Total Tasks: 0", bd=1, relief=tk.SUNKEN, anchor=tk.W)
    status_label.pack(side=tk.BOTTOM, fill=tk.X)

    load_tasks()
    root.bind('<Return>', lambda event: add_task())
    root.mainloop()

if __name__ == "__main__":
    main()