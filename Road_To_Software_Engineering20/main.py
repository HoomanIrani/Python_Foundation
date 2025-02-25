import datetime

date = datetime.date(2024, 12, 31)
today = datetime.date.today()
time = datetime.time(14, 14, 7)
now = datetime.datetime.now()

now = now.strftime("%H:%M:%S %d-%m-%Y")

print(today)
print(date)
print(time)
print(now)
print()

# target datetime program

target_datetime = datetime.datetime(2030, 1, 2, 12, 30, 1)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target date has passed!")
else:
    print("Target date has not passed!")
print()


# Alarm clock project
import time
import datetime
import pygame

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = "01 Taghdir.mp3"

    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time == alarm_time:
            print("Wake up! 😩")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(1)

            is_running = False

        time.sleep(1)

def main():
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)

if __name__ == "__main__":
    main()