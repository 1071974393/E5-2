import time

def focus_timer(minutes):
    seconds = minutes * 60
    print(f"Focus timer set for {minutes} minutes.")
    time.sleep(seconds)
    print("Time's up! Take a break.")

focus_timer(25)  # Start a 25-minute focus session
