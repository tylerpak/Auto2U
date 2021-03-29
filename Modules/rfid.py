import time
from datetime import datetime
import sys, select

class RFID:
    def __init__(self):
        pass

    def tag_detected(self):
        return False

def input_with_timeout(timeout=0.5):
    i, o, e = select.select( [sys.stdin], [], [], timeout)
    if (i):
        return sys.stdin.readline().strip()
    else:
        return ''

if __name__ == '__main__':
    time.sleep(5)
    print(input_with_timeout(0.1))
