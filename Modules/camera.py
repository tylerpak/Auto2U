#Must install OpenCV on RPI


import cv2
import datetime




# Initializing video capture obj


def capture_image(channel):
    camera = VideoCapture(channel)
    ret, new_frame = camera.read()
    cv2.imwrite(datetime.datetime.now() + ".jpg", new_frame)
    cv2.destroyAllWindows()
    print("Created image file")
    print("Done")
    camera.release()


if __name__ == '__main__':
   capture_image(0)