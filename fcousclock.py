import time

def focus_timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = "{:02d}:{:02d}".format(mins, secs)
        print(f"Remaining time: {timer}", end="\r")
        time.sleep(1)
        seconds -= 1
    print("Time's up! Stay focused!")

# 设置专注时长为25分钟
focus_timer(25)
