# Main Auto2U program
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
from Modules.client import TestClient, CloudClient
from Modules.rfid import RFID
from Modules.camera import Camera
from Modules.sound import SoundModule
import time
import datetime

def main():
    led_blue = LED(13)
    led_red = LED(15)

    while(True):
        print('Starting on-guard mode')
        led_blue.off()
        led_red.on()
        on_guard()

        print('Starting safety mode')
        led_blue.on()
        led_red.off()
        safety()



def on_guard():
    # Initialize for intrusion detection
    vibrationsensor = VibrationSensor(12)
    client = TestClient(id=42)
    rfid = RFID()

    # Loop until intrusion detected or RFID detected
    while (True):
        if vibrationsensor.is_vibrating():
            print('Possible intrusion detected')

            # # Capture 10 seconds of video
            # fps = 4
            # camera = Camera()
            # front_channel, back_channel = camera.capture_10s(fps=fps)

            # Check if user is present for the final time
            if rfid.tag_detected():
                print('RFID tag detected! Returning to safety mode.')
                return  # to safety mode

            print('Intrusion definitely detected. Sending info to cloud')

            # Send a video
            timestamp = datetime.datetime.now()
            for i in range(fps*10):
                print(f'sending frame {i}')
                # _, img_front = cv2.imencode('.jpg', front_channel[i])
                # client.send_video_frame(0, timestamp, img_front, i, fps*10, fps)
                # _, img_back = cv2.imencode('.jpg', back_channel[i])
                # client.send_video_frame(0, timestamp, img_back, i, fps*10, fps)

            # Query for user response. TODO: maybe exit this loop after 2min no response?
            while(True):
                if client.query_all_clear():
                    print('All clear')
                    client.reset_all_clear()
                    break
                if client.query_play_alarm():
                    while not client.query_all_clear():
                        print('Panic')
                        sound = SoundModule()
                        sound.play()
                    client.reset_all_clear()
                    client.reset_play_alarm()
                    break

        elif rfid.tag_detected():
            print('RFID tag detected! Returning to safety mode.')
            return  # To safety mode
        
def safety():
    # TODO: see safety flowchart; return when rfid tag no longer detected
    pass

if __name__ == '__main__':
    main()
    
