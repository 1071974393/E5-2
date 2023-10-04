import time

def focus_timer(minutes):
    seconds = minutes * 60
    start_time = time.time()
    end_time = start_time + seconds

    print(f"专注时钟开始，时长 {minutes} 分钟。")

    while time.time() < end_time:
        remaining_time = int(end_time - time.time())
        minutes_left = remaining_time // 60
        seconds_left = remaining_time % 60
        time_left = f"{minutes_left:02d}:{seconds_left:02d}"
        print(f"剩余时间：{time_left}", end="\r")
        time.sleep(1)

    print("\n专注时钟结束！")

# 设置专注时长为25分钟
focus_timer(25)
