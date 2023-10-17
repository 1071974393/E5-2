import tkinter as tk

def countdown():
    global time_remaining
    if time_remaining <= 0:
        root.destroy()
        # 在时间结束后可以执行一些操作，比如播放音乐或者打开其他的应用
    else:
        mins, secs = divmod(time_remaining, 60)
        timer_label.config(text='{:02d}:{:02d}'.format(mins, secs))
        time_remaining -= 1
        root.after(1000, countdown)

root = tk.Tk()
root.title('专注时钟')
time_remaining = 25 * 60  # 设置初始时间为25分钟
timer_label = tk.Label(root, text='25:00', font=('Helvetica', 48))
timer_label.pack(pady=20)
countdown_button = tk.Button(root, text='开始计时', command=countdown)
countdown_button.pack()
root.mainloop()

