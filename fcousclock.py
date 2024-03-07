import time
import winsound

def focus_timer(minutes):
    seconds = minutes * 60
    print(f"专注时间为 {minutes} 分钟")
    time.sleep(seconds)
    winsound.Beep(1000, 1000)  # 响铃提醒
    print("专注时间已结束！")

# 设置专注时间长度（以分钟为单位）
focus_time = 25

focus_timer(focus_time)
