import time
from datetime import datetime
import sys, select

class RFID:
    def __init__(self):
        pass

    def tag_detected(self):
        return input_with_timeout(0.1) != ''

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
    output = ''
    ser = serial.Serial('/dev/hidraw3', 4800, 8, 'N', 1, timeout=1)
    while True:
        print ("----")
        while output != "":
            output = get_serial(ser)
            print (output)
        output = " "
