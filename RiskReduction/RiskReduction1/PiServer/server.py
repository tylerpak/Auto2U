# Python socket server that sends 10 seconds of video upon request.
# Protocol: size of image, followed by byte stream of image itself; signal end with image size = 0.
# Loosely based on: https://www.youtube.com/watch?v=bWwZF_zVf00&ab_channel=TechWithTim

import io
import socket
import struct
import time
from PiServer.camera import Camera

# Initializations
stream = io.BytesIO()
camera = Camera(stream)
server_socket = socket.socket()
server_socket.bind(('', 8000))
server_socket.listen(0)

# Listen for requests
while(True):
    print('Listening for requests.')
    connection = server_socket.accept()[0].makefile('wb')
    try:
        print('Received request. Fetching 20 images at ~2 frames / second')
        for i in range(20):
            camera.captureToStream()  # Capture image into buffer
            connection.write(struct.pack('<L', stream.tell()))  # Send size of image
            connection.flush()
            stream.seek(0)
            connection.write(stream.read())  # Send encoded image from buffer
            stream.seek(0)
            stream.truncate()
            time.sleep(0.5)
        connection.write(struct.pack('<L', 0))  # Signal end of transmission with size 0
    finally:
        connection.close()
