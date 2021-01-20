# Test client for Python video socket server.
# Makes a connection request and listens

import io
import socket
import struct
from PIL import Image
import matplotlib.pyplot as pl

# Connect to server on localhost
client_socket = socket.socket()
client_socket.connect(('127.0.0.1', 8000))
connection = client_socket.makefile('rb')  # Read connection like a file.

try:
    img = None
    while True:
        # Quit loop when zero is received
        image_len = struct.unpack('<L', connection.read(struct.calcsize('<L')))[0]
        if not image_len:
            break

        # Read image into stream
        image_stream = io.BytesIO()
        image_stream.write(connection.read(image_len))
        image_stream.seek(0)
        image = Image.open(image_stream)
        
        if img is None:
            img = pl.imshow(image)
        else:
            img.set_data(image)

        pl.pause(0.01)
        pl.draw()

        print('Image is %dx%d' % image.size)
        image.verify()
        print('Image is verified')
finally:
    connection.close()
    client_socket.close()
    print('Client exiting')
