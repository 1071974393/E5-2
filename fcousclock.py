import time

def focus_timer(duration_minutes):
    duration_seconds = duration_minutes * 60
    end_time = time.time() + duration_seconds

    print(f"专注倒计时开始，持续 {duration_minutes} 分钟.")

    while time.time() < end_time:
        remaining_seconds = int(end_time - time.time())
        minutes, seconds = divmod(remaining_seconds, 60)
        print(f"剩余时间: {minutes:02d}:{seconds:02d}", end='\r')
        time.sleep(1)

    print("\n时间到！专注结束。")

if __name__ == "__main__":
    focus_duration = 25  # 专注时间（分钟）
    focus_timer(focus_duration)
