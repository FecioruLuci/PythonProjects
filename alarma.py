import time
import datetime
import contextlib
with contextlib.redirect_stdout(None):
    import pygame


def alarma(set_alarma):
    print(f"Ai alarma pentru ora {set_alarma}")
    sound_file = "W:/vscode/proiecte personale/Water Leak.mp3"
    merge = True

    while merge:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        print(now)
        time.sleep(1)
        if now == set_alarma:
            print("ALARMAAAA!!!")
            pygame.mixer.init()
            pygame.mixer_music.load(sound_file)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)
            merge = False
        
            

if __name__ == "__main__":
    set_alarma = input("Scrie la cat vrei alarma (ora):(minut):(secunda)")
    azi = datetime.datetime.now()
    print("Data de astazi este\n")
    azi = azi.strftime(" %H:%M:%S--%d--%m--%Y")
    print(azi)
    alarma(set_alarma)
