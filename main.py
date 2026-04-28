import tkinter as tk

def add_task():
    task = task_entry.get()
    if task:
        listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except:
        pass

def main():
    global task_entry, listbox
    root = tk.Tk()
    root.title("Student Planner App")
    root.geometry("400x500")
    
    tk.Label(root, text="My Student Planner", font=("Arial", 16, "bold")).pack(pady=10)
    task_entry = tk.Entry(root, width=30)
    task_entry.pack(pady=5)

    tk.Button(root, text="Add Task", command=add_task, bg="green", fg="white").pack(pady=5)
    tk.Button(root, text="Delete Selected Task", command=delete_task, bg="red", fg="white").pack(pady=5)

    listbox = tk.Listbox(root, width=45, height=15)
    listbox.pack(pady=10)

    
    root.bind('<Return>', lambda event: add_task())

    root.mainloop()

if __name__ == "__main__":
    main()