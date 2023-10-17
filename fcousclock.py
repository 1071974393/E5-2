import time

def focus_timer(total_time, break_time):
    while total_time > 0:
        print(f"专注时间剩余：{total_time} 秒")
        time.sleep(1)
        total_time -= 1
        if total_time == 0:
            print("休息时间！")
            time.sleep(break_time)
            total_time = int(input("请输入下一轮专注时间（秒）："))

if __name__ == "__main__":
    total_time = int(input("请输入专注时间（秒）："))
    break_time = int(input("请输入休息时间（秒）："))
    focus_timer(total_time, break_time)
