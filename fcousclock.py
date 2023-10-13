import time

def focus_timer(duration):
    print("专注时钟开始")
    for remaining in range(duration, 0, -1):
        minutes, seconds = divmod(remaining, 60)
        timeformat = f"{minutes:02d}:{seconds:02d}"
        print(timeformat, end='\r')
        time.sleep(1)
    print("专注时钟结束")

if __name__ == "__main__":
    focus_duration = 25 * 60  # 25分钟，可以根据需要调整
    focus_timer(focus_duration)
