import time

def focus_timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer_display = f"{mins:02d}:{secs:02d}"
        print(f"Focus Timer: {timer_display}", end='\r')
        time.sleep(1)
        seconds -= 1
    print("\nTime's up! Take a break.")

if __name__ == "__main__":
    try:
        focus_time = int(input("请输入专注时长（分钟）: "))
        print(f"专注时钟已启动，时长: {focus_time} 分钟")
        focus_timer(focus_time)
    except ValueError:
        print("无效的输入，请输入一个整数分钟数。")
