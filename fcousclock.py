import time

def focus_timer(minutes):
    seconds = minutes * 60
    while seconds:
        mins, secs = divmod(seconds, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        seconds -= 1
    print("专注时间到！")

if __name__ == "__main__":
    tasks = ["任务1", "任务2", "任务3", "任务4"]
    focus_times = [25, 30, 20, 35]  # 每个任务的专注时间（分钟）

    for i in range(len(tasks)):
        task_name = tasks[i]
        focus_minutes = focus_times[i]
        print(f"开始专注于任务: {task_name}")
        focus_timer(focus_minutes)
        print(f"任务: {task_name} 完成\n")

    print("所有任务已完成！")
