import tkinter as tk

def greet():
    name = entry.get()
    greeting_label.config(text=f"Hello, {name}!")

# Set up the main window
root = tk.Tk()
root.title("Name Entry App")

# Create and place widgets
entry = tk.Entry(root)
entry.pack(pady=10)

greet_button = tk.Button(root, text="Greet", command=greet)
greet_button.pack(pady=5)

greeting_label = tk.Label(root, text="")
greeting_label.pack(pady=10)

# Run the application
root.mainloop()
