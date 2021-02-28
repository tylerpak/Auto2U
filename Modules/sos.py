import RPi.GPIO as GPIO
import time
from datetime import datetime

class SOSButton:
    def __init__(self, input_pin=25):
        self.input_pin = input_pin
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.input_pin, GPIO.IN)

    def is_ready(self):
        i=GPIO.input(self.input_pin)
        if i == 0:
            return False
        elif i == 1:
            print(f'SOS button pressed at {datetime.now()}')
            return True


if __name__ == '__main__':
    sos = SOSButton()
    while(1):
        print(sos.is_ready())
        time.sleep(1)
