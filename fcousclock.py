import tkinter as tk
from tkinter import messagebox
import time

def start_timer():
    try:
        minutes = int(entry.get())
        seconds = minutes * 60
        while seconds:
            mins, secs = divmod(seconds, 60)
            timer_label.config(text=f'{mins:02d}:{secs:02d}')
            window.update()
            time.sleep(1)
            seconds -= 1
        messagebox.showinfo("专注时间结束", "专注时间已结束！")
    except ValueError:
        messagebox.showerror("错误", "请输入有效的分钟数")

window = tk.Tk()
window.title("专注时钟")

instruction_label = tk.Label(window, text="请输入专注的分钟数：")
instruction_label.pack(pady=10)

entry = tk.Entry(window)
entry.pack()

start_button = tk.Button(window, text="开始专注", command=start_timer)
start_button.pack(pady=10)

timer_label = tk.Label(window, text="", font=("Helvetica", 48))
timer_label.pack()

window.mainloop()
