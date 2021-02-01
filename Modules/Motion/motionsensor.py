import RPi.GPIO as GPIO
import time
from datetime import datetime

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)         #Read output from PIR motion sensor
i = 0

while True:
    i=GPIO.input(11)
    print(i)
    if i==0:                 #When output from motion sensor is LOW
        print(f"No intruders: {datetime.now()}")
        time.sleep(0.5)
    elif i==1:               #When output from motion sensor is HIGH
        print(f"Intruder detected: {datetime.now()}")
        time.sleep(0.5)

