import time
import tkinter as tk
from tkinter import messagebox

def start_focus_timer(minutes):
    seconds = minutes * 60
    time.sleep(seconds)
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("专注提醒", f"专注时间已结束！")
    root.destroy()

# 设置专注时间长度（以分钟为单位）
focus_time = 25

start_focus_timer(focus_time)
