import time

def focus_timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timeformat = f"{mins:02d}:{secs:02d}"
        print(f"专注倒计时: {timeformat}", end='\r')
        time.sleep(1)
        seconds -= 1

    print("\n专注时间结束！")

if __name__ == "__main__":
    focus_minutes = 30
    focus_timer(focus_minutes)
