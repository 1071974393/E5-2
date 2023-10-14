import time

def focus_timer(minutes):
    seconds = minutes * 60
    while seconds:
        mins, secs = divmod(seconds, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        seconds -= 1
    print("专注时间到！")

if __name__ == "__main__":
    focus_minutes = 25  # 设置专注时间为25分钟
    focus_timer(focus_minutes)
