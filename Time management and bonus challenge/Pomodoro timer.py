#Pomodoro Timer: Create a program that implements the Pomodoro Technique (25 minutes 
#work, 5 minutes break). Use a loop and if statements to track time intervals and notify the user 
#when to switch between work and breaks
from datetime import datetime, timedelta
import time
start=input("")
current = datetime.now()
formatted = current.strftime("%I:%M %p")
format = datetime.strptime(formatted, "%I:%M %p")
notify_time = format + timedelta(minutes=25)
time.sleep(25*60)
print("Take Break :)")
current = datetime.now()
formatted = current.strftime("%I:%M %p")
format = datetime.strptime(formatted, "%I:%M %p")
notify_time = format + timedelta(minutes=5)
time.sleep(5*60)
print("Break End :(")

















