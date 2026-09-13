import datetime
import time
import pygame
def main(set_time):
    print(f"The alarm is set for {set_time}")
    sound_path="Alarm Clock.mp3"
    is_running=True
    while is_running:
        current_time=datetime.datetime.now().strftime("%H:%M:%S")
        print(f"The current time: {current_time}")
        if current_time==set_time:
            print("Wake up 🕗 🌄 !")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_path)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(1)
            is_running=False
        elif set_time < current_time:
            print(f"The timing '{set_time}' has already passed!")
            is_running=False
        else:
            time.sleep(1)
if __name__=='__main__':
    while True:
        set_time=input("Enter the alarm you want to set(H:M:S): ")
        try:
            datetime.datetime.strptime(set_time, "%H:%M:%S")
            break
        except Exception:
            print("Invalid time! USE:'HH:MM:SS' format")

    main(set_time)
