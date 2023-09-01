import time

def focus_timer(minutes):
    seconds = minutes * 60
    start_time = time.time()
    end_time = start_time + seconds
    
    print(f"Focus timer set for {minutes} minutes.")
    
    while time.time() < end_time:
        remaining_time = int(end_time - time.time())
        minutes_left = remaining_time // 60
        seconds_left = remaining_time % 60
        
        print(f"Time left: {minutes_left:02d}:{seconds_left:02d}", end="\r", flush=True)
        time.sleep(1)
    
    print("\nFocus timer expired. Time to take a break!")

# 设置专注时间为25分钟
focus_timer(25)
