import time

def focus_timer(minutes):
    seconds = minutes * 60
    try:
        while seconds:
            mins, secs = divmod(seconds, 60)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            print(f"剩余时间: {timeformat}", end='\r')
            time.sleep(1)
            seconds -= 1

        print("\n时间到！专注时间已结束。")

    except KeyboardInterrupt:
        print("\n专注时钟已被中断。")

if __name__ == "__main__":
    try:
        minutes = int(input("请输入专注时间（分钟）："))
        focus_timer(minutes)
    except ValueError:
        print("无效的输入。请输入一个整数分钟数。")
