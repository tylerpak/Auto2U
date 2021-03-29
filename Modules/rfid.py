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

if __name__ == '__main__':
    rfid = RFID()
    for i in range(10):
        print(f'Looking for RFID {i}/10')
        time.sleep(1)
        if input_with_timeout():
            print('RFID found')
        else:
            print('No RFID found')
