import time

def focus_timer(duration):
    print("开始专注...")
    time.sleep(duration * 60)
    print("专注时间结束！")

# 设置专注时长（以分钟为单位）
focus_duration = 25

# 启动专注时钟
focus_timer(focus_duration)
