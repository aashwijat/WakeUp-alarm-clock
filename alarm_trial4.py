from playsound import playsound
import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def alarm(seconds):
    time_elapse = 0

    print(CLEAR)
    while time_elapse < seconds:
        time.sleep(1)
        time_elapse+=1

        time_left = seconds - time_elapse
        hours_left = time_left // 3600
        minutes_left = time_left // 60
        secs_left = time_left%60

        print(f"{CLEAR_AND_RETURN}Alarm will play in : {hours_left:02d}:{minutes_left:02d}:{secs_left:02d}")

    playsound("dynamite.mp3")

hours = int(input("number of hours : "))
minutes = int(input("number of minutes : "))
seconds = int(input("number of seconds : "))

total_secs = hours*3600 + minutes*60 + seconds
alarm(total_secs)

