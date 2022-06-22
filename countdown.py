
import time
import datetime

# take user input for time counted down
hours = int(input("Hours: "))
minutes = int(input("Minutes: "))
seconds = int(input("Seconds: "))
tot_secs = hours * 3600 + minutes * 60 + seconds

# display timer
while tot_secs:
    timer = datetime.timedelta(seconds = tot_secs)
    print(timer, end = "\r")
    time.sleep(1)
    tot_secs -= 1
        
# tell user when  time is up
print("Time up!!")