import os
import time

class SoundModule():
    def __init__(self, audio_file='alarm.wav'):
        self.file = audio_file

    def play(self, filename="Modules/alarm.wav"):
        os.system(f"omxplayer {filename}")
        time.sleep(1)

if __name__ == "__main__":
    sm = SoundModule()
    sm.play()

