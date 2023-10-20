import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print('Break Time!')
    # 循环 5 分钟休息计时器
    countdown(5*60)

countdown(25*60)
