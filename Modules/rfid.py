import time
from datetime import datetime
import sys, select


class RFID:

    def __init__(self):
        self.value = False

    def tag_detected(self):
        
        file = open("Modules/rfid_in.txt", 'w+')
        rfid_tag = file.read()
        if rfid_tag != '' and rfid_tag is not None:
            print('Detected Tag')
            self.value = self.value ^ True
            file.truncate(0)
        file.close()

        return self.value
            
            
        


