import time
import threading

def focus_timer(minutes, timer_id):
    seconds = minutes * 60
    while seconds:
        mins, secs = divmod(seconds, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(f"Timer {timer_id}: {timeformat}", end='\r')
        time.sleep(1)
        seconds -= 1
    print(f"Timer {timer_id} 完成！")

if __name__ == "__main__":
    timers = []
    focus_minutes = 25  # 设置专注时间为25分钟

    for i in range(1, 5):  # 创建4个专注时钟
        timer = threading.Thread(target=focus_timer, args=(focus_minutes, i))
        timers.append(timer)
        timer.start()

    for timer in timers:
        timer.join()

    print("所有专注时钟完成！")
