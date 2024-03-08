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
        
        hours_remaining = remaining_time // 3600
        minutes_remaining = (remaining_time % 3600) // 60
        seconds_remaining = remaining_time % 60
        
        print(f"Time remaining: {int(hours_remaining):02d} hours {int(minutes_remaining):02d} minutes {int(seconds_remaining):02d} seconds")
        time.sleep(1)

focus_timer(60)
