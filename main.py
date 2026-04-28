import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Student Planner App")
    root.geometry("400x400")
    
    label = tk.Label(root, text="Welcome to your Student Planner", font=("Arial", 14))
    label.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()