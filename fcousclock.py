import time

def concentration_timer(minutes):
    seconds = minutes * 60
    start_time = time.time()
    end_time = start_time + seconds

    while time.time() < end_time:
        remaining_time = int(end_time - time.time())
        print(f"Remaining time: {remaining_time} seconds")
        time.sleep(1)

    print("Time's up! Focus session completed.")

# 设置专注时长为25分钟（调整为你需要的时间）
concentration_timer(25)
