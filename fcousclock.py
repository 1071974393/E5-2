import tkinter as tk
import asyncio


async def count_down(seconds, label):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        label.config(text='{:02d}:{:02d}'.format(mins, secs))
        await asyncio.sleep(1)
        seconds -= 1
    label.config(text="Time's up!")


def start_timer(minutes):
    loop = asyncio.get_event_loop()

    def on_start():
        loop.create_task(count_down(minutes * 60, timer_label))

    def on_exit():
        loop.stop()
        window.destroy()

    # 创建窗口
    window = tk.Tk()
    window.title("Focus Timer")
    window.protocol("WM_DELETE_WINDOW", on_exit)

    # 创建计时标签
    timer_label = tk.Label(window, text='', font=('Arial', 30))
    timer_label.pack(expand=True)

    # 创建开始和退出按钮
    button_frame = tk.Frame(window)
    button_frame.pack(expand=True)

    start_button = tk.Button(button_frame, text="Start", command=on_start)
    start_button.pack(side=tk.LEFT, padx=5)

    exit_button = tk.Button(button_frame, text="Exit", command=on_exit)
    exit_button.pack(side=tk.RIGHT, padx=5)

    loop.run_forever()
    loop.close()

start_timer(25)  # 25分钟的专注时钟
```
