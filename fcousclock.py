import time
import sys

def countdown_timer(duration_in_minutes):
    try:
        duration_in_seconds = duration_in_minutes * 60
        for remaining in range(duration_in_seconds, 0, -1):
            sys.stdout.write("\r")
            mins, secs = divmod(remaining, 60)
            timeformat = f"{mins:02d}:{secs:02d}"
            sys.stdout.write(f"剩余时间: {timeformat} ")
            sys.stdout.flush()
            time.sleep(1)
        print("\n专注时钟结束！")
    except KeyboardInterrupt:
        print("\n专注时钟已中断。")

if __name__ == "__main__":
    minutes = int(input("请输入专注时钟的持续时间（分钟）："))
    countdown_timer(minutes)
