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
from Modules.GPS import GPS
from Modules.sos import SOSButton
import cv2
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
    print('Setting up on guard')
    # Initialize for intrusion detection
    vibrationsensor = VibrationSensor(12)
    client = TestClient(id=42)
    rfid = RFID()
    gps_module = GPS()

    # Loop until intrusion detected or RFID detected
    while (True):
        print('Looping on guard')
        if vibrationsensor.is_vibrating():
            print('Possible intrusion detected')

            # Capture 10 seconds of video
            fps = 1
            camera = Camera()
            front_channel, back_channel = camera.capture_10s(fps=fps)

            # Check if user is present for the final time
            if rfid.tag_detected():
                print('RFID tag detected! Returning to safety mode.')
                return  # to safety mode

            print('Intrusion definitely detected. Sending info to cloud')

            # Send a video
            timestamp = datetime.datetime.now()
            for i in range(fps*10):
                print(f'sending frame {i}')
                _, img_front = cv2.imencode('.jpg', front_channel[i])
                client.send_video_frame(0, timestamp, img_front, i, fps*10, fps)
                _, img_back = cv2.imencode('.jpg', back_channel[i])
                client.send_video_frame(1, timestamp, img_back, i, fps*10, fps)

            # Query for user response. TODO: maybe exit this loop after 2min no response?
            while(True):
                # Alarm section here twice for testing with test server that always sends True for Ret_val
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
                if client.query_send_video():
                    timestamp = datetime.datetime.now()
                    for i in range(fps*10):
                        print(f'sending frame {i}')
                        _, img_front = cv2.imencode('.jpg', front_channel[i])
                        client.send_video_frame(0, timestamp, img_front, i, fps*10, fps)
                        _, img_back = cv2.imencode('.jpg', back_channel[i])
                        client.send_video_frame(1, timestamp, img_back, i, fps*10, fps)
                        time.sleep(2)

        elif rfid.tag_detected():
            print('RFID tag detected! Returning to safety mode.')
            return  # To safety mode
        
def safety():
    print('Setting up safety mode')


    init_time = datetime.datetime.now()
    frame_count = 0

    #initialize camerea, gps, SOS, RFID, motion, and vibration modules
    camera = Camera()
    gps_module = GPS()
    sosButton = SOSButton()
    rfid = RFID()
    motionsensor = MotionSensor()
    client = TestClient(id=42)
    
    #Check conditions to see if user is in car
    while True:
        print('Looping safety')

        #If SOS button is pressed, send warning to AMS and start recording video
        if sosButton.is_ready():

            client.send_sos_warning()
            lat, lng = gps_module.getPositionData()
            client.send_gps(lng, lat)
            front_channel, back_channel = camera.capture_10s(fps=fps)

            timestamp = datetime.datetime.now()
            for i in range(fps*10):
                print(f'sending frame {i}')
                _, img_front = cv2.imencode('.jpg', front_channel[i])
                client.send_video_frame(0, timestamp, img_front, i, fps*10, fps)
                _, img_back = cv2.imencode('.jpg', back_channel[i])
                client.send_video_frame(1, timestamp, img_back, i, fps*10, fps)

            #Wait for all clear sign from AMS
            while(not client.query_all_clear()):
                print("Waiting for all clear!")
                time.sleep(5)
       
        #If RFID tag is not there, then wait for no motion and then switch to on-guard mode
        elif not rfid.tag_detected():
            print("No tag has been detecting, waiting for user to leave then returning to on-guard mode.")
            break
        
        #If user is determined to still be in the car, record background video in 10 second segments
        front = camera.capture_front()
        back = camera.capture_back()
        cv2.imwrite(f'Background/front/{init_time.strftime("%m-%d-%Y, %H:%M:%S")}_{frame_count}.jpg', front)
        cv2.imwrite(f'Background/back/{init_time.strftime("%m-%d-%Y, %H:%M:%S")}_{frame_count}.jpg', back)
        frame_count += 1

    # Wait for user to leave vehicle
    print('waiting 10 seconds for user to leave')
    time.sleep(10)
    print('waiting until motion is not sensed for 10 seconds')
    motion_detected = True
    motionsensor = MotionSensor(11)
    while (motion_detected):
        motion_detected = False
        # look for motion for 10 seconds
        t_end = time.time() + 10
        while time.time() < t_end:
            if motionsensor.is_moving():
                print('Motion detected. Waiting another 10s')
                motion_detected = True
                break
        
    print('User has now left vehicle. Performing safety functions')

    return

if __name__ == '__main__':
    main()
    
