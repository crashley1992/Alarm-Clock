import time
import datetime

# gets current time
result = time.localtime()

# setting varable for hour, minute, seconds so it can be added to user input
current_hour = result.tm_hour
current_min = result.tm_min
current_sec = result.tm_sec

# test to make sure format is correct
print(f'{current_hour} : {current_min} : {current_sec}')

# asks for user input for alarm
hour_input = input('How many hours from now would you like the timer to be set: ')
hour_set = int(hour_input)
min_input = input('How many minutes from now would you like the timer to be set: ')
min_set = int(min_input)
sec_input = input('How many seconds from now would you like the timer to be set: ' )
sec_set = int(sec_input)


def alarm():
    print(f'Current time is {current_hour}:{current_min}:{current_sec}')
    # takes user input an added to time object
    alarm_hour = current_hour + hour_set 
    alarm_min = current_min + min_set
    alarm_sec = current_sec + sec_set

    # 
    alarm_string = f'{alarm_hour}:{alarm_min}:{alarm_sec}'
    
    print(f'Alarm set for {alarm_hour}:{alarm_min}:{alarm_sec}')

    now = datetime.datetime.now()

    my_datetime = datetime.datetime.strptime(alarm_string, "%H:%M:%S")

    my_datetime = now.replace(hour=my_datetime.time().hour, minute=my_datetime.time().minute, second=my_datetime.time().second, microsecond=0)

    if now > my_datetime:
        print('beep')
    
       

       
alarm()