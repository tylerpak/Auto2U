import time
from datetime import datetime
import sys, select
import serial
import evdev

class RFID:
    def __init__(self, event=0):
        self.device = evdev.InputDevice(f'/dev/input/event{event}')
        print(self.device)
        self.curr_val = False

    def tag_detected(self):
        start = time.time()
        detected = False
        for event in self.device.read_loop():
            print('Hello')
            
            
        if count > 0:
            return True


