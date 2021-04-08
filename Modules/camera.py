#Must install OpenCV on RPI

import cv2
import datetime
import time

class Camera:
    def __init__(self):
        self.initialize_cameras()
        record = True

    def initialize_cameras(self):
        idx = 0
        front_idx = 0
        back_idx = 0
        while True:
            print('searching idx ' + str(idx))
            cam = cv2.VideoCapture(idx)
            if cam.read()[0]:
                print('found front idx ' + str(idx))
                front_idx = idx
                idx += 1
                cam.release()
                break
            else:
                idx += 1
                if idx > 100:
                    print('WARNING: could not find camera in 100 indexes.')
                    return

        while True:
            print('searching idx ' + str(idx))
            cam = cv2.VideoCapture(idx)
            if cam.read()[0]:
                print('found back idx ' + str(idx))
                back_idx = idx
                idx += 1
                cam.release()
                break
            else:
                idx += 1
                if idx > 100:
                    print('WARNING: could not find camera in 100 indexes.')
                    return

        self.front_idx = front_idx
        self.back_idx = back_idx
        print('Camera initialization complete')

    def capture_front(self):
        print('Capturing front image')
        camera = cv2.VideoCapture(self.front_idx)
        ret, new_frame = camera.read()
        if ret == False:
            print('WARNING: could not find frame')
        print("Done")
        camera.release()
        return new_frame

    def capture_back(self):
        print('Capturing back image')
        camera = cv2.VideoCapture(self.back_idx)
        ret, new_frame = camera.read()
        if ret == False:
            print('WARNING: could not find frame')
        print("Done")
        camera.release()
        return new_frame

    def capture_10s(self, fps=1):
        print('Capturing 10 seconds of images on both channels')
        seconds = 10
        frames = seconds * fps
        delay = 1/fps
        front_channel, back_channel = [], []

        for i in range(frames):
            print(f'Frame {i}/{frames}')
            front_channel.append(self.capture_front())
            back_channel.append(self.capture_back())
        
        return front_channel, back_channel
    
    def capture_background(self, fps):
        print('Beginning background recording on both channels')
        codec = cv2.VideoWriter_fourcc(*'DIVX')
        front, back = [], []
        delay = 1/fps
        test = 200
        for i in range(test):
            front.append(self.capture_front())
            back.append(self.capture_back())
            time.sleep(delay)
        out1 = cv2.VideoWriter('front.avi', codec, 24, (640, 480))
        for i in range(len(front)):
            out1.write(front[i])
        out2 = cv2.VideoWriter('back.avi', codec, 24, (640, 480))
        for i in range(len(back)):
            out2.write(back[i])
            
            
if __name__ == '__main__':
    camera = Camera()

#     front, back = camera.capture_10s(4)
#     for i in range(len(front)):
#         cv2.imwrite(f"imgs/front_{i}.jpg", front[i])
#         cv2.imwrite(f"imgs/back_{i}.jpg", back[i])
    camera.capture_background(0.5)
    
