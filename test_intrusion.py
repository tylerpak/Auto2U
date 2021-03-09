# Testing intrusion detection
# Hardware interface:
#   Motion sensor data pin:     PIN 11
#   Vibration sensor data pin:  PIN 12
#   LED Blue:                   PIN 13
#   LED RED:                    PIN 15
#   Speaker:                    AUX

from Modules.motionsensor import MotionSensor
from Modules.vibrationsensor import VibrationSensor
from Modules.sound import SoundModule
from Modules.led import LED
import time


# Setup
led_blue = LED(13)
led_red = LED(15)
motion = MotionSensor(11)
vibration = VibrationSensor(12)

while(True):
    if motion.is_moving():
        led_blue.on()
        time.sleep(1)
        led_blue.off()
    if vibration.is_vibrating():
        led_red.on()
        time.sleep(1)
        led_red.off()
