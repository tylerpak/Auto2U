from gps import *
import time

running = True

def getPositionData(gps):
    nx = gpsd.next()
    while nx['class'] != 'TPV':
        nx = gpsd.next()
        
    if nx['class'] == 'TPV':
        latitude = getattr(nx, 'lat', "Unknown")
        longitude = getattr(nx, 'lon', "Unknown")
        print("Your position: lon = "+str(longitude)+", lat = "+str(latitude))
        location = (latitude, longitude)
        
gpsd = gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE)

try:
    print("Application started")
    getPositionData(gpsd)
except (KeyboardInterrupt):
    running = False
    print('Applications closed')