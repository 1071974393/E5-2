import time

def focus_timer(minutes):
    seconds = minutes * 60
    for remaining_time in range(seconds, 0, -1):
        mins, secs = divmod(remaining_time, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(f"Focus Timer: {timeformat}", end='\r')
        time.sleep(1)
    print("\nTime's up! Take a break.")

if __name__ == "__main__":
    minutes = int(input("请输入专注时长（分钟）: "))
    focus_timer(minutes)
