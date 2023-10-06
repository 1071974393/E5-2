import tkinter as tk
import time

# 创建一个窗口
window = tk.Tk()
window.title("专注时钟")

# 设置初始时间（以秒为单位）
remaining_time = 25 * 60  # 25分钟

# 显示剩余时间的标签
time_label = tk.Label(window, text="", font=("Helvetica", 48))
time_label.pack()

# 更新剩余时间的函数
def update_time():
    global remaining_time
    if remaining_time > 0:
        minutes = remaining_time // 60
        seconds = remaining_time % 60
        time_label.config(text=f"{minutes:02d}:{seconds:02d}")
        remaining_time -= 1
        window.after(1000, update_time)  # 每秒更新一次
    else:
        time_label.config(text="时间到！")

# 开始计时
def start_timer():
    global remaining_time
    if remaining_time > 0:
        start_button.config(state=tk.DISABLED)
        update_time()

# 创建开始按钮
start_button = tk.Button(window, text="开始", command=start_timer)
start_button.pack()

# 运行窗口
window.mainloop()
