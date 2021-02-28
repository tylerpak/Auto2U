#Must install OpenCV on RPI


import cv2
import datetime




# Initializing video capture obj
    

def capture_image(channel):
    camera = cv2.VideoCapture(channel)
    ret, new_frame = camera.read()
    now = datetime.datetime.now()
    date = now.strftime("%H:%M:%S_%m_%d_%Y")
    cv2.imwrite(date + ".jpg", new_frame)
    cv2.destroyAllWindows()
    print("Created image file")
    print("Done")
    camera.release()


if __name__ == '__main__':
   capture_image(0)