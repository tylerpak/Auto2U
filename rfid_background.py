import evdev

device = evdev.InputDevice(f'/dev/input/event0')

#file = open("Modules/rfid_in.txt",'w')
for event in device.read_loop():
    file = open("Modules/rfid_in.txt",'w')  
    file.write(event)
    file.close()


