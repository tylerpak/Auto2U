import time
from datetime import datetime
import sys, select


class RFID:

    def __init__(self):
        self.value = False

    def tag_detected(self):
        
        file = open("Modules/rfid_in.txt", 'r')
        rfid_tag = file.read()
        if rfid_tag != '' and rfid_tag is not None:
            print('Detected Tag')
            if self.value:
                self.value = False
            else:
                self.value = True
            file.close()
            file = open("Modules/rfid_in.txt", 'w')
            file.close()
        else:
            file.close()

        return self.value
            

if __name__ == '__main__':
    rfid = RFID()
    while True:
        print(rfid.tag_detected())
        time.sleep(1)


