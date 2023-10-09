import tkinter as tk
import time

# 创建一个窗口
window = tk.Tk()
window.title("专注时钟")

# 设置初始时间（以秒为单位）
initial_time = 25 * 60  # 25分钟

# 创建显示时间的标签
time_label = tk.Label(window, text="")
time_label.pack()

# 定义一个函数来更新时间
def update_time():
    global initial_time
    if initial_time > 0:
        minutes, seconds = divmod(initial_time, 60)
        time_label.config(text=f"{minutes:02d}:{seconds:02d}")
        initial_time -= 1
        window.after(1000, update_time)  # 每隔1秒更新一次时间
    else:
        time_label.config(text="时间到！")

# 创建开始按钮
start_button = tk.Button(window, text="开始", command=update_time)
start_button.pack()

# 运行窗口
window.mainloop()
