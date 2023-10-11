import time
import os

def focus_timer(duration_in_minutes):
    duration_in_seconds = duration_in_minutes * 60
    while duration_in_seconds:
        mins, secs = divmod(duration_in_seconds, 60)
        timeformat = f"{mins:02d}:{secs:02d}"
        os.system("clear")  # For Unix/Linux
        # os.system("cls")  # For Windows
        print(f"专注时钟剩余时间: {timeformat}", end="\r")
        time.sleep(1)
        duration_in_seconds -= 1

    print("\n专注时钟结束！")

if __name__ == "__main__":
    minutes = int(input("请输入专注时钟的持续时间（分钟）："))
    focus_timer(minutes)
