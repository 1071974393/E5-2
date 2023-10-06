import time
import winsound

def focus_timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        seconds -= 1

    # 专注时间结束后的提醒音
    frequency = 1500  # 提醒音频率（以赫兹为单位）
    duration = 2000  # 提醒音持续时间（以毫秒为单位）
    winsound.Beep(frequency, duration)
    print("时间到！专注时间结束。")

# 设置专注时间为25分钟
focus_timer(25)
