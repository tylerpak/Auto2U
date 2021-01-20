# Wrapper for camera capture
# Uses OpenCV to read camera frames into a buffer

import cv2

class Camera:
    def __init__(self, stream):
        '''
        Initialize camera capture module
        :param stream: stream at which to write camera output (probably BytesIO stream)
        '''
        self.camera = cv2.VideoCapture(0)
        self.stream = stream

    def captureToStream(self):
        '''
        Capture a frame and write to the output stream.
        '''
        ret, frame = self.camera.read()
        if not ret:
            print("failed to grab frame")
            return
        is_success, buffer = cv2.imencode(".jpg", frame)
        if not is_success:
            print("Failed to encode frame")
        self.stream.write(buffer)
