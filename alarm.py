import time
from datetime import datetime
import winsound

# gets current time
result = time.localtime()

# setting varable for hour, minute, seconds so it can be added to user input
current_hour = result.tm_hour
current_min = result.tm_min
current_sec = result.tm_sec

# test to make sure format is correct
print(f'{current_hour} : {current_min} : {current_sec}')

# asks for user input for alarm, all converted to int for time.sleep() in alarm function
hour_input = input('How many hours from now would you like the timer to be set: ')
hour_set = int(hour_input)
min_input = input('How many minutes from now would you like the timer to be set: ')
min_set = int(min_input)
sec_input = input('How many seconds from now would you like the timer to be set: ' )
sec_set = int(sec_input)

# alarm sound that goes off
def sound():
	for i in range(2): # Number of repeats

		for j in range(9): # Number of beeps
			
			winsound.MessageBeep(-1) # Sound played
		
		time.sleep(2) # How long between beeps

# displays time and uses time.sleep() to delay sound() by converting all input to seconds and inputing it into the time.sleep()
def alarm():
    print(f'Current time is {current_hour}:{current_min}:{current_sec}')
    # takes user input an added to time object
    alarm_hour = current_hour + hour_set 
    alarm_min = current_min + min_set
    alarm_sec = current_sec + sec_set
    
    print(f'Alarm set for {alarm_hour}:{alarm_min}:{alarm_sec}')

    # counter variable that will take in the amount of delay for time.sleep()
    seconds_to_wait = 0

    # converstons for user's time input
    if hour_set > 0:
        # times 60 twice to get converstion from hours to seconds
        wait_time = (hour_set * 60) * 60
        # adds variable to seconds to wait counter
        seconds_to_wait += wait_time

    elif min_set > 0:
        # times 60 once to get converstion from minutes to seconds
        wait_time = (min_set * 60)
        seconds_to_wait += wait_time

    elif sec_set > 0:
        wait_time = sec_set
        seconds_to_wait += wait_time

    time.sleep(seconds_to_wait)
    # wanted a visual indicator for those who may not hear
    print('Beep!')
    sound()


alarm()