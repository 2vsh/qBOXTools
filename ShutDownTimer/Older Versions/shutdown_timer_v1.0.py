import tkinter as tk
from tkinter import messagebox
import time
import os

def start_shutdown_timer():
    try:
        minutes = int(entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number of minutes.")
        return
    
    if minutes < 1:
        messagebox.showerror("Error", "Please enter a positive number of minutes.")
        return

    time.sleep(minutes * 60)
    os.system("shutdown /s /t 1")

def on_start_button_click():
    window.withdraw()
    start_shutdown_timer()

window = tk.Tk()
window.title("Shutdown Timer")

frame = tk.Frame(window)
frame.pack(padx=10, pady=10)

label = tk.Label(frame, text="Enter the number of minutes till shutdown:")
label.pack(padx=5, pady=5)

entry = tk.Entry(frame)
entry.pack(padx=5, pady=5)

start_button = tk.Button(frame, text="Start", command=on_start_button_click)
start_button.pack(padx=5, pady=5)

window.mainloop()
