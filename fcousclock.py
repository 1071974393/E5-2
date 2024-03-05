import time
import winsound

def focus_timer(minutes):
    seconds = minutes * 60
    for i in range(seconds, 0, -1):
        print(f"Time remaining: {i//60} minutes {i%60} seconds", end='\r')
        time.sleep(1)
    print("Time's up!")
    winsound.Beep(1000, 1000)  # Beep for 1 second

focus_timer(25)  # Start a 25-minute focus session
