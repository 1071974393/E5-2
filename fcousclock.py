import time

def countdown(minutes):
    seconds = minutes * 60
    while seconds > 0:
        print(f"Remaining Time: {seconds // 60} minutes {seconds % 60} seconds", end="\r")
        time.sleep(1)
        seconds -= 1

    print("Time's up!")

work_time = 25  # 设置工作时间为25分钟
countdown(work_time)
