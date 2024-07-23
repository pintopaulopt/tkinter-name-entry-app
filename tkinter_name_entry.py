import tkinter as tk

def on_submit():
    name = entry.get()
    label.config(text=f"Hello, {name}!")

root = tk.Tk()
root.title("Name Entry App")

label = tk.Label(root, text="Enter your name:")
label.pack()

entry = tk.Entry(root)
entry.pack()

submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack()

root.mainloop()
