import tkinter as tk

COLORS = ["black", "white", "red", "green", "blue"]

class PixelTest(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("{0}x{1}+0+0".format(self.winfo_screenwidth(), self.winfo_screenheight()))
        self.attributes('-fullscreen', True)
        self.configure(background=COLORS[0])
        self.bind("<Escape>", lambda e: self.quit())
        self.bind("<space>", self.change_color)
        self.color_index = 0

    def change_color(self, event):
        self.color_index = (self.color_index + 1) % len(COLORS)
        self.configure(background=COLORS[self.color_index])

if __name__ == "__main__":
    app = PixelTest()
    app.mainloop()
