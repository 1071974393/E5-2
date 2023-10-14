import time

def focus_timer(focus_minutes, break_minutes):
    focus_seconds = focus_minutes * 60
    break_seconds = break_minutes * 60

    while focus_seconds:
        mins, secs = divmod(focus_seconds, 60)
        timeformat = 'Focus: {:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        focus_seconds -= 1

    print("专注时间结束！")
    
    while break_seconds:
        mins, secs = divmod(break_seconds, 60)
        timeformat = 'Break: {:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        break_seconds -= 1

if __name__ == "__main__":
    focus_minutes = 25  # 设置专注时间为25分钟
    break_minutes = 5   # 设置休息时间为5分钟
    focus_timer(focus_minutes, break_minutes)
