from gps import *
import time

class GPS:
    def __init__(self):
        self.gpsd = gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE)

    def getPositionData(self):
        nx = self.gpsd.next()
        while nx['class'] != 'TPV':
            nx = self.gpsd.next()
            
        if nx['class'] == 'TPV':
            latitude = getattr(nx, 'lat', "Unknown")
            longitude = getattr(nx, 'lon', "Unknown")
            print("Your position: lon = "+str(longitude)+", lat = "+str(latitude))
            location = (latitude, longitude)
            return location

        else:
            return (0,0)
        
if __name__ == '__main__':
    module = GPS()
    while True:
        pos = module.getPositionData()
        print(pos)
        time.sleep(1)