import tkinter as tk

def add_task():
    
    task = task_entry.get()
    if task:
        print(f"Task Added: {task}")
        task_entry.delete(0, tk.END) 

def main():
    global task_entry
    
    root = tk.Tk()
    root.title("Student Planner App")
    root.geometry("400x400")
    
    
    label = tk.Label(root, text="My Student Planner", font=("Arial", 16, "bold"))
    label.pack(pady=10)

    
    inst_label = tk.Label(root, text="Enter a new task below:")
    inst_label.pack()

   
    task_entry = tk.Entry(root, width=30)
    task_entry.pack(pady=5)

    
    add_button = tk.Button(root, text="Add Task", command=add_task, bg="green", fg="white")
    add_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()