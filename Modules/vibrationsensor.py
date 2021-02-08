import RPi.GPIO as GPIO
import time
from datetime import datetime

class VibrationSensor:
    def __init__(self, input_pin=11):
        self.input_pin = input_pin
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.input_pin, GPIO.IN)

    def is_vibrating(self):
        i=GPIO.input(self.input_pin)
        if i == 0:
            print(f'No vibration detected at {datetime.now()}')
            return False
        elif i == 1:
            print(f'Vibration detected at {datetime.now()}')
            return True


if __name__ == '__main__':
    vibrationsensor = VibrationSensor(input_pin=11)
    while(1):
        print(vibrationsensor.is_vibrating())
        time.sleep(1)

