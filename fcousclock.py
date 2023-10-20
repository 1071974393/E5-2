import time

def focus_timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        # 计算剩余时间的小时、分钟、秒数
        hours, remainder = divmod(seconds, 3600)
        mins, secs = divmod(remainder, 60)
        
        # 格式化时间显示
        timer = "{:02d}:{:02d}:{:02d}".format(hours, mins, secs)
        
        # 输出剩余时间并更新
        print("Remaining time: {}".format(timer), end="\r")
        
        # 等待1秒
        time.sleep(1)
        
        # 减去1秒的时间
        seconds -= 1
    
    print("Time's up! Stay focused!")

# 设置专注时长为45分钟
focus_timer(45)
