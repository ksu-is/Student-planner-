import tkinter as tk
import json
import os

DATA_FILE = "tasks.json"

def save_tasks():
    tasks = listbox.get(0, tk.END)
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f)

def load_tasks():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            tasks = json.load(f)
            for task in tasks:
                listbox.insert(tk.END, task)

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

def main():
    global task_entry, listbox
    root = tk.Tk()
    root.title("Student Planner App")
    root.geometry("400x550")
    
    tk.Label(root, text="My Student Planner", font=("Arial", 16, "bold")).pack(pady=10)
    task_entry = tk.Entry(root, width=30)
    task_entry.pack(pady=5)

    tk.Button(root, text="Add Task", command=add_task, bg="green", fg="white").pack(pady=5)
    tk.Button(root, text="Delete Selected Task", command=delete_task, bg="red", fg="white").pack(pady=5)

    listbox = tk.Listbox(root, width=45, height=15)
    listbox.pack(pady=10)

    load_tasks()
    
    root.bind('<Return>', lambda event: add_task())
    root.mainloop()

if __name__ == "__main__":
    main()