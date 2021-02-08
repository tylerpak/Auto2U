import RPi.GPIO as GPIO
import time
from datetime import datetime

class MotionSensor:
    def __init__(self, input_pin=11):
        self.input_pin = input_pin
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.input_pin, GPIO.IN)

    def is_moving(self):
        i=GPIO.input(self.input_pin)
        if i == 0:
            print(f'No motion detected at {datetime.now()}')
            return False
        elif i == 1:
            print(f'Motion detected at {datetime.now()}')
            return True


if __name__ == '__main__':
    motionsensor = MotionSensor()
    while(1):
        print(motionsensor.is_moving())
        time.sleep(1)

