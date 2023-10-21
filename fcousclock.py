import time

def focus_timer(minutes):
    seconds = minutes * 60
    while seconds:
        mins, secs = divmod(seconds, 60)
        timeformat = f'{mins:02d}:{secs:02d}'
        print(f'Focus Timer: {timeformat}', end='\r')
        time.sleep(1)
        seconds -= 1
    print('\nTime\'s up! Take a break.')

if __name__ == "__main__":
    try:
        minutes = int(input("请输入专注时长（分钟）: "))
        focus_timer(minutes)
    except ValueError:
        print("无效的输入，请输入一个整数分钟数。")

