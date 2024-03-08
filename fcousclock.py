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
        
        print(f"Time remaining: {int(remaining_time/60)} minutes {int(remaining_time%60)} seconds")
        time.sleep(1)

focus_timer(25)
