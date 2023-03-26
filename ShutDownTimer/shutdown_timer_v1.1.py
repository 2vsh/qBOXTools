import os
import time
import tkinter as tk
from tkinter import ttk

def start_countdown():
    try:
        hours = int(hours_var.get()) if hours_var.get().isdigit() else 0
        minutes = int(minutes_var.get()) if minutes_var.get().isdigit() else 0
        seconds = int(seconds_var.get()) if seconds_var.get().isdigit() else 0
        total_seconds = hours * 3600 + minutes * 60 + seconds
    except ValueError:
        return

    for i in range(total_seconds, -1, -1):
        remaining_time.set(f"Remaining time: {i // 3600:02d}:{(i % 3600) // 60:02d}:{i % 60:02d}")
        window.update()
        time.sleep(1)

    os.system("shutdown /s /t 1")

window = tk.Tk()
window.title("Shutdown Timer")

frame = ttk.Frame(window, padding="10")
frame.grid(row=0, column=0)

hours_var = tk.StringVar()
minutes_var = tk.StringVar()
seconds_var = tk.StringVar()
remaining_time = tk.StringVar()

ttk.Label(frame, text="Hours:").grid(column=0, row=0)
ttk.Entry(frame, width=5, textvariable=hours_var).grid(column=1, row=0)

ttk.Label(frame, text="Minutes:").grid(column=0, row=1)
ttk.Entry(frame, width=5, textvariable=minutes_var).grid(column=1, row=1)

ttk.Label(frame, text="Seconds:").grid(column=0, row=2)
ttk.Entry(frame, width=5, textvariable=seconds_var).grid(column=1, row=2)

ttk.Button(frame, text="Start Countdown", command=start_countdown).grid(column=0, row=3, columnspan=2)

ttk.Label(frame, textvariable=remaining_time).grid(column=0, row=4, columnspan=2)

window.mainloop()
