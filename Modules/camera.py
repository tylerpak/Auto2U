#Must install OpenCV on RPI
from multiprocessing.context import Process

import cv2
from video_capture import VideoCaptureAsync
import time
import datetime



width = 1920
height = 1080

# Initializing video capture obj
camera = VideoCaptureAsync(src=0, width=width, height=height)

codec = cv2.VideoWriter_fourcc(*'DIVX')


def is_recording(duration):
    camera.start()
    end = time.time() + duration
    frames = 0
    images = []
    while time.time() <= end:
        ret, new_frame = camera.read()
        frames += 1
        images.append(new_frame)
    camera.stop()
    fps = frames/duration
    print("FPS: " + fps)
    print("Total images taken " + images)
    out = cv2.VideoWriter(datetime.datetime.now() + ".avi", codec, fps, (width, height))
    print("Creating Video File")
    for i in range(len(images)):
        out.write(images[i])
    images = []
    print("Done")


if __name__ == '__main__':
   duration = 20
   record = Process(target = is_recording, args= (duration, ))
   record.start()
   record.join()
   record.close()
