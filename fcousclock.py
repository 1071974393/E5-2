import tkinter as tk
from tkinter import messagebox
import time

class FocusTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("专注时钟")

        self.minutes = tk.StringVar(value=25)
        self.seconds = tk.StringVar(value=0)

        self.label = tk.Label(root, textvariable=self.format_time(), font=("Helvetica", 48))
        self.label.pack(pady=20)

        self.start_button = tk.Button(root, text="开始", command=self.start_timer)
        self.start_button.pack()

    def format_time(self):
        minutes = self.minutes.get()
        seconds = self.seconds.get()
        return f"{minutes:02d}:{seconds:02d}"

    def start_timer(self):
        self.minutes.set(int(self.minutes.get()))
        self.seconds.set(int(self.seconds.get()))

        total_seconds = int(self.minutes.get()) * 60 + int(self.seconds.get())

        for i in range(total_seconds, -1, -1):
            minutes, seconds = divmod(i, 60)
            self.minutes.set(minutes)
            self.seconds.set(seconds)
            self.label.config(text=self.format_time())
            self.root.update()
            time.sleep(1)

        messagebox.showinfo("专注时钟", "时间到！")
        self.minutes.set(25)
        self.seconds.set(0)
        self.label.config(text=self.format_time())

if __name__ == "__main__":
    root = tk.Tk()
    app = FocusTimer(root)
    root.mainloop()

