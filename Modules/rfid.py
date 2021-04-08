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

def input_with_timeout(timeout=0.5):
    i, o, e = select.select( [sys.stdin], [], [], timeout)
    if (i):
        return sys.stdin.readline().strip()
    else:
        return ''

    

def get_serial(ser):
    return ser.readline()



if __name__ == '__main__':
    rfid = RFID()
    #output = ''
    #ser = serial.Serial('/dev/input/event4', 9600, timeout=1)
    #while True:
    #    print ("----")
    #    while output != "":
    #        output = ser.readline().decode('UTF-8').strip()
    #        print (output)
    #        output = ""

    while True:
        print(rfid.tag_detected())
