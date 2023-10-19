import time

def focus_timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print("专注倒计时: " + timeformat, end='\r')
        time.sleep(1)
        seconds -= 1

    print("\n专注时间结束！")

if __name__ == "__main__":
    try:
        focus_minutes = int(input("请输入专注的分钟数："))
        focus_timer(focus_minutes)
    except ValueError:
        print("无效的输入。请输入一个整数分钟数。")
