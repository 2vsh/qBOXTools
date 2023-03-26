import tkinter as tk
from tkinter import messagebox, simpledialog
import time
import os

class CustomDialog(simpledialog.Dialog):
    def body(self, master):
        tk.Label(master, text="Do you want to hide the program or quit?").grid(row=0, sticky=tk.W)
        return None

    def buttonbox(self):
        box = tk.Frame(self)

        tk.Button(box, text="Quit", width=10, command=self.quit).grid(row=0, column=0, padx=5, pady=5)
        tk.Button(box, text="Hide", width=10, command=self.hide).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(box, text="Cancel", width=10, command=self.cancel).grid(row=0, column=2, padx=5, pady=5)

        self.bind("<Return>", self.cancel)
        self.bind("<Escape>", self.cancel)

        box.pack()

    def quit(self):
        self.result = "quit"
        self.destroy()

    def hide(self):
        self.result = "hide"
        self.destroy()

    def cancel(self, event=None):
        self.result = "cancel"
        self.destroy()

def start_shutdown_timer():
    hours = int(hour_entry.get() or 0)
    minutes = int(minute_entry.get() or 0)
    seconds = int(second_entry.get() or 0)

    if hours < 0 or minutes < 0 or seconds < 0:
        messagebox.showerror("Error", "Please enter positive numbers for hours, minutes, and seconds.")
        return

    sleep_time = hours * 3600 + minutes * 60 + seconds
    time.sleep(sleep_time)

    if option_var.get() == "Shutdown":
        os.system("shutdown /s /t 1")
    elif option_var.get() == "Restart":
        os.system("shutdown /r /t 1")
    elif option_var.get() == "Sleep":
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

def on_start_button_click():
    start_shutdown_timer()

def on_close():
    dialog = CustomDialog(window)
    result = dialog.result

    if result == 'hide':
        window.withdraw()
    elif result == 'quit':
        window.quit()

window = tk.Tk()
window.protocol("WM_DELETE_WINDOW", on_close)
window.title("Shutdown Timer")

frame = tk.Frame(window)
frame.pack(padx=10, pady=10)

label = tk.Label(frame, text="Enter the time till shutdown (hours, minutes, seconds):")
label.pack(padx=5, pady=5)

hour_label = tk.Label(frame, text="Hours:")
hour_label.pack(side='left', padx=5, pady=5)
hour_entry = tk.Entry(frame, width=5)
hour_entry.pack(side='left', padx=5, pady=5)

minute_label = tk.Label(frame, text="Minutes:")
minute_label.pack(side='left', padx=5, pady=5)
minute_entry = tk.Entry(frame, width=5)
minute_entry.pack(side='left', padx=5, pady=5)

second_label = tk.Label(frame, text="Seconds:")
second_label.pack(side='left', padx=5, pady=5)
second_entry = tk.Entry(frame, width=5)
second_entry.pack(side='left', padx=5, pady=5)

start_button = tk.Button(frame, text="Start", command=on_start_button_click)
start_button.pack(padx=5, pady=5)

option_var = tk.StringVar()
option_var
option_var.set("Shutdown")

options = ["Shutdown", "Restart", "Sleep"]
option_menu = tk.OptionMenu(frame, option_var, *options)
option_menu.pack(padx=5, pady=5)

window.mainloop()
