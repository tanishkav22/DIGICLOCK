import tkinter as tk
import time
from tkinter import colorchooser

# Create main window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("420x220")
root.resizable(False, False)

# Default theme values
bg_color = "#ffffff"
text_color = "#000000"

root.configure(bg=bg_color)

# Clock label
clock_label = tk.Label(
    root,
    font=("DS-Digital", 48, "bold"),
    bg=bg_color,
    fg=text_color
)
clock_label.pack(pady=30)

# Function to update time
def update_time():
    current_time = time.strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)

# Light theme
def light_mode():
    root.configure(bg="#ffffff")
    clock_label.configure(bg="#ffffff", fg="#000000")

# Dark theme
def dark_mode():
    root.configure(bg="#1e1e1e")
    clock_label.configure(bg="#1e1e1e", fg="#00ffcc")

# Change font color
def change_color():
    color = colorchooser.askcolor()[1]
    if color:
        clock_label.config(fg=color)

# Buttons frame
btn_frame = tk.Frame(root, bg=bg_color)
btn_frame.pack(pady=10)

# Buttons
tk.Button(
    btn_frame, text="Light Mode", width=10,
    command=light_mode
).grid(row=0, column=0, padx=5)

tk.Button(
    btn_frame, text="Dark Mode", width=10,
    command=dark_mode
).grid(row=0, column=1, padx=5)

tk.Button(
    btn_frame, text="Font Color", width=10,
    command=change_color
).grid(row=0, column=2, padx=5)

# Start clock
update_time()

# Run app
root.mainloop()
