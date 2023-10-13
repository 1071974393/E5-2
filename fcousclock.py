import time

def focus_timer(duration, task_name):
    print(f"{task_name}专注时钟开始")
    for remaining in range(duration, 0, -1):
        minutes, seconds = divmod(remaining, 60)
        timeformat = f"{minutes:02d}:{seconds:02d}"
        print(timeformat, end='\r')
        time.sleep(1)
    print(f"{task_name}专注时钟结束")

if __name__ == "__main__":
    break_duration = 5 * 60  # 5分钟休息时长
    break_task_name = "休息"  # 任务名称
    focus_timer(break_duration, break_task_name)
