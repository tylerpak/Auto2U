import RPi.GPIO as GPIO
import time

class LED:
    def __init__(self, output_pin=11):
        self.output_pin = output_pin
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.output_pin, GPIO.OUT)

    def on(self):
        GPIO.output(self.output_pin, GPIO.HIGH)

    def off(self):
        GPIO.output(self.output_pin, GPIO.LOW)

if __name__ == '__main__':
    blue = LED(13)
    red = LED(15)
    blue.on()
    time.sleep(1)
    blue.off()
    red.on()
    time.sleep(1)
    red.off()
