import time

def focus_timer(duration):
    print("开始专注...")
    end_time = time.time() + duration * 60
    while time.time() < end_time:
        remaining_time = int(end_time - time.time())
        mins, secs = divmod(remaining_time, 60)
        timer_display = "{:02d}:{:02d}".format(mins, secs)
        print(timer_display, end="\r")
        time.sleep(1)
    print("专注时间结束！")

# 设置专注时长（以分钟为单位）
focus_duration = 25

# 启动专注时钟
focus_timer(focus_duration)

