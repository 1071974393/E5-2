import time

def focus_timer(minutes):
    seconds = minutes * 60
    print(f"Focus timer set for {minutes} minutes.")
    for i in range(seconds, 0, -1):
        print(f"Time remaining: {i//60} minutes {i%60} seconds", end='\r')
        time.sleep(1)
    print("Time's up! Take a break.")

focus_timer(25)  # Start a 25-minute focus session
