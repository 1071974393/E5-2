import tkinter as tk
from tkinter import messagebox

def start_timer():
    minutes = int(entry.get())
    seconds = minutes * 60
    countdown(seconds)

def countdown(seconds):
    if seconds >= 0:
        mins, secs = divmod(seconds, 60)
        timer_label.config(text="{:02d}:{:02d}".format(mins, secs))
        root.after(1000, countdown, seconds-1)
        # 每秒钟更新剩余时间并递归调用自身
    else:
        messagebox.showinfo("时间到！", "专注时间已结束！")

root = tk.Tk()
root.title("专注时钟")

entry_label = tk.Label(root, text="请输入专注时间（分钟）：")
entry_label.pack()

entry = tk.Entry(root)
entry.pack()

start_button = tk.Button(root, text="开始", command=start_timer)
start_button.pack()

timer_label = tk.Label(root, font=("Helvetica", 36), pady=20)
timer_label.pack()

root.mainloop()
