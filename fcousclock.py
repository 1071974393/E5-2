import time
import tkinter as tk

def start_timer():
    global is_running
    is_running = True
    update_timer()

def stop_timer():
    global is_running
    is_running = False

def reset_timer():
    global is_running
    is_running = False
    elapsed_time.set(25 * 60)

def update_timer():
    if is_running and elapsed_time.get() > 0:
        elapsed_time.set(elapsed_time.get() - 1)
        root.after(1000, update_timer)
    elif elapsed_time.get() == 0:
        is_running = False
        # 在这里可以添加专注结束的提醒

is_running = False

root = tk.Tk()
root.title("专注时钟")

elapsed_time = tk.IntVar()
elapsed_time.set(25 * 60)

time_label = tk.Label(root, textvariable=elapsed_time, font=("Helvetica", 48))
time_label.pack()

start_button = tk.Button(root, text="开始", command=start_timer)
stop_button = tk.Button(root, text="停止", command=stop_timer)
reset_button = tk.Button(root, text="重置", command=reset_timer)

start_button.pack()
stop_button.pack()
reset_button.pack()

root.mainloop()
