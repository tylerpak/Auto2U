import os
import time

def play():
    ### Plays approx. 20 seconds of alarm
    print("Playing ~20s of sound")
    os.system("omxplayer alarm.wav")
    time.sleep(1)

if __name__ == "__main__":
    play()

