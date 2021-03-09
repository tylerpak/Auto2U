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
import time

def main():
    # Control flow between safety and on guard modes.

    ## Initializations (TODO: More needed; only initialize what's needed to save power)
    print('Initializing')
    motionsensor = MotionSensor(11)
    vibrationsensor = VibrationSensor(12)

    while(True):
        print('Starting on-guard mode')
        on_guard(motionsensor, vibrationsensor)
        print('Starting safety mode')
        safety()


def on_guard(motionsensor, vibrationsensor):
    # On-guard mode: detect intrusion or owner return to vehicle
    time.sleep(5)    # Ensure owner is done leaving vehicle

    # Define behavior when passenger is in car and when car is empty
    def on_guard_passenger_in_car():
        ## Someone is in vehcile; monitor surroundings
        # TODO: monitor camera surroundings and save to SD card; return when RFID tag is detected
        pass

    def on_guard_intrusion_detection():
        ## No one is in vehicle; detect intrusions with vibration sensor

        while (True):
            if vibrationsensor.is_vibrating():
                print('Possible intrusion detected')
                # TODO: follow flowchart
                #   - If RFID tag detected: return to safety mode
                #   - Else: Record 10s video and notify user and wait for response (play sound, all clear, etc.)
                #   - resume loop once user gives all clear

            elif True: # replace 'True' with rfid tag is detected
                print('Owner returning to vehicle')
                return

            time.sleep(0.5)

    # Initially see if anyone is still in the car- check for motion for 10 seconds
    initial_movement_detected = False
    while(initial_movement_detected):
        for i in range(20):
            initial_movement_detected |= motionsensor.is_moving()
            time.sleep(0.5)

    if initial_movement_detected:
        print('Passenger in car. Monitoring surroundings.')
        on_guard_passenger_in_car()

    else:
        print('No passenger in car. Starting intrusion detection.')
        on_guard_intrusion_detection()

        
def safety():
    # TODO: see safety flowchart; return when rfid tag no longer detected
    pass

if __name__ == '__main__':
    main()
    
