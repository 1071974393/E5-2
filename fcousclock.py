import tkinter as tk
from tkinter import messagebox
import time

# 创建主窗口
root = tk.Tk()
root.title("专注时钟")

# 设置初始时间（以秒为单位）
initial_time = 25 * 60  # 25分钟

# 创建计时器变量
current_time = tk.StringVar()
current_time.set(time.strftime("%M:%S", time.gmtime(initial_time)))

# 更新时间显示
def update_time():
    global initial_time
    if initial_time > 0:
        initial_time -= 1
        current_time.set(time.strftime("%M:%S", time.gmtime(initial_time)))
        root.after(1000, update_time)
    else:
        messagebox.showinfo("时间到", "休息一下！")
        initial_time = 25 * 60
        current_time.set(time.strftime("%M:%S", time.gmtime(initial_time)))

# 创建显示时间的标签
time_label = tk.Label(root, textvariable=current_time, font=("Helvetica", 48))
time_label.pack(pady=20)

# 创建开始按钮
start_button = tk.Button(root, text="开始", command=update_time)
start_button.pack()

# 创建退出按钮
quit_button = tk.Button(root, text="退出", command=root.quit)
quit_button.pack()

# 运行主循环
root.mainloop()
