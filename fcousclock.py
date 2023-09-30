import time
import sys

def countdown(minutes):
    seconds = minutes * 60
    while seconds:
        mins, secs = divmod(seconds, 60)
        timeformat = f"{mins:02d}:{secs:02d}"
        sys.stdout.write(f"剩余时间: {timeformat}\r")
        sys.stdout.flush()
        time.sleep(1)
        seconds -= 1

    print("\n时间到！专注时间已结束。")

if __name__ == "__main__":
    try:
        minutes = int(input("请输入专注时间（分钟）："))
        countdown(minutes)
    except ValueError:
        print("无效的输入。请输入一个整数分钟数。")
