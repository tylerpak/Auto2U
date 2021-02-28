#Must install OpenCV on RPI

import cv2
import datetime

class Camera:
    def __init__(self):
        self.initialize_cameras()

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

if __name__ == '__main__':
    camera = Camera()

    frame = camera.capture_front()
    cv2.imwrite("front.jpg", frame)

    frame = camera.capture_back()
    cv2.imwrite("back.jpg", frame)
