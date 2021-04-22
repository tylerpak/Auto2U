from gps import *
import time

class GPS:
    def __init__(self):
        self.gpsd = gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE)
        self.last_loc = (30.284340,-97.743710)

    def getPositionData(self):
        nx = self.gpsd.next()
        # while nx['class'] != 'TPV':
        #     nx = self.gpsd.next()

        print(nx)
        
        if nx['class'] == 'TPV':
            latitude = getattr(nx, 'lat', "Unknown")/100.0
            longitude = getattr(nx, 'lon', "Unknown")/100.0
            print("Your position: lon = "+str(longitude)+", lat = "+str(latitude))
            location = (latitude, longitude)
            self.last_loc = location
            return location

        else:
            return self.last_loc
        
if __name__ == '__main__':
    module = GPS()
    while True:
        pos = module.getPositionData()
        print(pos)
        time.sleep(1)