import time

def countdown(n):
    while n > 0:
        print(n)
        n -= 1
        time.sleep(1)
    print("时间到！")

n = 25 # 计时器时间，单位为分钟
countdown(n*60) # 将时间换算为秒数传入计时器函数中
