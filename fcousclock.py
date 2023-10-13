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
    work_duration = 25 * 60  # 25分钟工作时长
    work_task_name = "工作"  # 任务名称
    focus_timer(work_duration, work_task_name)

