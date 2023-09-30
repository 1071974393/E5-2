import time
import datetime

def focus_timer(minutes):
    # 计算结束时间
    end_time = datetime.datetime.now() + datetime.timedelta(minutes=minutes)

    while datetime.datetime.now() < end_time:
        remaining_time = end_time - datetime.datetime.now()
        print(f"剩余时间: {remaining_time}", end='\r')
        time.sleep(1)

    print("时间到！专注时间已结束。")

if __name__ == "__main__":
    try:
        minutes = int(input("请输入专注时间（分钟）："))
        focus_timer(minutes)
    except ValueError:
        print("无效的输入。请输入一个整数分钟数。")
