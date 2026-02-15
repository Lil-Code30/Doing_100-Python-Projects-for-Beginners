from datetime import datetime
import time

def get_current_time():
    return datetime.now().strftime("%I:%M %p")


alarm_time = input("Set alarm time (e.g., 07:30 AM): ")
print(f"Alarm set to {alarm_time}. Waiting...")

while True:
    curret_time = get_current_time()
    
    if alarm_time == curret_time:
        print(f"Alarm! It's {alarm_time}. Time to wake up!")
        
    time.sleep(60)