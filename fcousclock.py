import time

def countdown(minutes):
    seconds = minutes * 60
    while seconds:
        mins, secs = divmod(seconds, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

def pomodoro_timer(work_minutes, short_break_minutes, long_break_minutes, cycles):
    for cycle in range(cycles):
        print(f"Cycle {cycle + 1} of {cycles}")
        print("Work time!")
        countdown(work_minutes)
        
        if cycle < cycles - 1:
            print("Short break time!")
            countdown(short_break_minutes)
        else:
            print("Long break time!")
            countdown(long_break_minutes)

if __name__ == "__main__":
    work_minutes = 25  # 工作时间25分钟
    short_break_minutes = 5  # 短暂休息时间5分钟
    long_break_minutes = 15  # 长时间休息时间15分钟
    cycles = 4  # 总共4个工作周期

    pomodoro_timer(work_minutes, short_break_minutes, long_break_minutes, cycles)
