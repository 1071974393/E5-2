import time

def focus_timer(minutes):
    seconds = minutes * 60
    start_time = time.time()
    
    while True:
        elapsed_time = time.time() - start_time
        remaining_time = seconds - elapsed_time
        
        if remaining_time <= 0:
            print("Focus timer finished!")
            break
        
        minutes_remaining = int(remaining_time / 60)
        seconds_remaining = int(remaining_time % 60)
        
        if minutes_remaining < 10:
            mins_display = f"0{minutes_remaining}"
        else:
            mins_display = str(minutes_remaining)
            
        if seconds_remaining < 10:
            secs_display = f"0{seconds_remaining}"
        else:
            secs_display = str(seconds_remaining)
            
        print(f"Time remaining: {mins_display}:{secs_display}")
        time.sleep(1)

focus_timer(45)
