import time

def concentration_timer(minutes):
    seconds = minutes * 60
    start_time = time.time()
    end_time = start_time + seconds

    while time.time() < end_time:
        remaining_time = int(end_time - time.time())
        minutes_left = remaining_time // 60
        seconds_left = remaining_time % 60
        print(f"Remaining time: {minutes_left:02d}:{seconds_left:02d}")
        time.sleep(1)

    print("Time's up! Focus session completed.")

# 设置专注时长为20分钟（调整为你需要的时间）
concentration_timer(20)
