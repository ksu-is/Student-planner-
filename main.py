import tkinter as tk
import json
import os
from tkinter import messagebox

DATA_FILE = "tasks.json"

def update_count():
    status_label.config(text=f"Total Tasks: {listbox.size()}")

def save_tasks():
    tasks = []

    for i in range(listbox.size()):
        tasks.append(listbox.get(i))

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
    assignment = assignment_entry.get()
    due_date = due_date_entry.get()
    time_estimate = time_entry.get()
    importance = importance_entry.get()
    stress = stress_entry.get()

    if assignment and due_date and time_estimate and importance and stress:
        task = f"{assignment} | Due: {due_date} | Time: {time_estimate} min | Importance: {importance}/10 | Stress: {stress}/10"

        listbox.insert(tk.END, task)

        assignment_entry.delete(0, tk.END)
        due_date_entry.delete(0, tk.END)
        time_entry.delete(0, tk.END)
        importance_entry.delete(0, tk.END)
        stress_entry.delete(0, tk.END)

        save_tasks()
    else:
        messagebox.showwarning("Missing Info", "Please fill out all task fields.")

def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
        save_tasks()
    except:
        messagebox.showwarning("No Selection", "Please select a task to delete.")

def clear_all():
    if messagebox.askyesno("Confirm", "Clear all tasks?"):
        listbox.delete(0, tk.END)
        save_tasks()

def main():
    global assignment_entry, due_date_entry, time_entry, importance_entry, listbox, status_label

    root = tk.Tk()
    root.title("Panic Panda Planner")
    root.geometry("550x650")

    tk.Label(root, text="Panic Panda Planner", font=("Arial", 18, "bold")).pack(pady=10)

    form_frame = tk.Frame(root)
    form_frame.pack(pady=10)

    tk.Label(form_frame, text="Assignment:").grid(row=0, column=0, sticky="w")
    assignment_entry = tk.Entry(form_frame, width=35)
    assignment_entry.grid(row=0, column=1, pady=5)

    tk.Label(form_frame, text="Due Date:").grid(row=1, column=0, sticky="w")
    due_date_entry = tk.Entry(form_frame, width=35)
    due_date_entry.grid(row=1, column=1, pady=5)

    tk.Label(form_frame, text="Time Estimate:").grid(row=2, column=0, sticky="w")
    time_entry = tk.Entry(form_frame, width=35)
    time_entry.grid(row=2, column=1, pady=5)

    tk.Label(form_frame, text="Importance 1-10:").grid(row=3, column=0, sticky="w")
    importance_entry = tk.Entry(form_frame, width=35)
    importance_entry.grid(row=3, column=1, pady=5)

    btn_frame = tk.Frame(root)
    btn_frame.pack(pady=10)

    tk.Button(btn_frame, text="Add Task", command=add_task, bg="green", fg="white", width=12).grid(row=0, column=0, padx=5)
    tk.Button(btn_frame, text="Delete Task", command=delete_task, bg="orange", fg="white", width=12).grid(row=0, column=1, padx=5)
    tk.Button(btn_frame, text="Clear All", command=clear_all, bg="red", fg="white", width=12).grid(row=0, column=2, padx=5)

    list_frame = tk.Frame(root)
    list_frame.pack(pady=10)

    scrollbar = tk.Scrollbar(list_frame, orient=tk.VERTICAL)
    listbox = tk.Listbox(list_frame, width=75, height=15, yscrollcommand=scrollbar.set)

    scrollbar.config(command=listbox.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    listbox.pack(side=tk.LEFT)

    status_label = tk.Label(root, text="Total Tasks: 0", bd=1, relief=tk.SUNKEN, anchor=tk.W)
    status_label.pack(side=tk.BOTTOM, fill=tk.X)

    load_tasks()

    root.bind("<Return>", lambda event: add_task())
    root.mainloop()

if __name__ == "__main__":
    main()