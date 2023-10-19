import time

def focus_timer(duration_in_minutes):
    duration_in_seconds = duration_in_minutes * 60
    print(f"专注时间开始，持续 {duration_in_minutes} 分钟.")
    time.sleep(duration_in_seconds)
    print("专注时间结束，可以休息一下！")

if __name__ == "__main__":
    focus_duration = int(input("请输入专注时间（分钟）: "))
    focus_timer(focus_duration)
