```python
import time

def focus_timer(minutes):
    seconds = minutes * 60
    print(f"Focus timer set for {minutes} minutes.")
    while seconds > 0:
        m, s = divmod(seconds, 60)
        timeformat = '{:02d}:{:02d}'.format(m, s)
        print("Time remaining:", timeformat, end='\r')
        time.sleep(1)
        seconds -= 1
    print("\nTime's up! Take a break.")

focus_timer(25)  # Start a 25-minute focus session
```
