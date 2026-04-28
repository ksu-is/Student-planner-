import tkinter as tk

def add_task():
    task = task_entry.get()
    if task:
        listbox.insert(tk.END, task) # This adds it to the list on screen
        task_entry.delete(0, tk.END)

def main():
    global task_entry, listbox
    root = tk.Tk()
    root.title("Student Planner App")
    root.geometry("400x500")
    
    tk.Label(root, text="My Student Planner", font=("Arial", 16, "bold")).pack(pady=10)
    task_entry = tk.Entry(root, width=30)
    task_entry.pack(pady=5)

    tk.Button(root, text="Add Task", command=add_task, bg="green", fg="white").pack(pady=10)

    
    listbox = tk.Listbox(root, width=45, height=15)
    listbox.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()