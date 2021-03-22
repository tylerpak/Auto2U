import RPi.GPIO as GPIO
import time
from datetime import datetime

class SOSButton:
    def __init__(self, input_pin=36, verbose=False):
        self.input_pin = input_pin
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.input_pin, GPIO.IN)
        self.verbose = verbose
        

    def is_ready(self):
        i=GPIO.input(self.input_pin)
        if i == 1:
            if self.verbose:
                print(f'SOS detected at {datetime.now()}')
                return True
        else:
            if self.verbose:
                return False


if __name__ == '__main__':
    sos = SOSButton()
    while(1):
        print(sos.is_ready())
        time.sleep(1)
        
