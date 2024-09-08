import datetime
import time
import os

def set_alarm(alarm_time, sound_file):
    print("Alarm is set for", alarm_time)
    while True:
        time.sleep(1)
        now = datetime.datetime.now()
        if now.hour == alarm_time.hour and now.minute == alarm_time.minute:
            print("Wake Up!")
            os.system(f'start {sound_file}')
            break

def main():
    alarm_hour = int(input("Enter the hour for the alarm: "))
    alarm_minute = int(input("Enter the minute for the alarm: "))
    sound_file = input("Enter the path to the sound file: ")
    alarm_time = datetime.datetime.now()
    alarm_time = alarm_time.replace(hour=alarm_hour, minute=alarm_minute, second=0)
    set_alarm(alarm_time, sound_file)

if __name__ == "__main__":
    main()