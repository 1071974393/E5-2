import datetime
import time

def focus_timer(minutes):
    end_time = datetime.datetime.now() + datetime.timedelta(minutes=minutes)
    
    while datetime.datetime.now() < end_time:
        remaining_time = end_time - datetime.datetime.now()
        timer = str(remaining_time).split(".")[0]
        print(timer, end="\r")
        time.sleep(1)

    print("时间到！")

if __name__ == "__main__":
    minutes = int(input("请输入要专注的分钟数："))
    focus_timer(minutes)
