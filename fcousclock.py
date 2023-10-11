import time

def focus_timer(duration_in_minutes):
    try:
        duration_in_seconds = duration_in_minutes * 60
        print(f"专注时钟启动，将持续 {duration_in_minutes} 分钟。")
        time.sleep(duration_in_seconds)
        print("专注时钟结束！")
    except KeyboardInterrupt:
        print("\n专注时钟已中断。")

if __name__ == "__main__":
    minutes = int(input("请输入专注时钟的持续时间（分钟）："))
    focus_timer(minutes)
