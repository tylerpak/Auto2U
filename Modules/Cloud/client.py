import requests
import json
import jsonpickle
import cv2

class Client:
    def __init__(self):
        pass

    def send_video_frame(self, img_encoded):
        pass

    def send_gps(self, lng, lat):
        pass

class TestClient(Client):
    ### Works with local test server
    def __init__(self):
        pass

    def send_video_frame(self, img_encoded):
        # img_encoded should already be encoded with cv2.imencode('.jpg', img)
        response = requests.post('http://localhost:5000/api/img', data=img_encoded.tostring(), headers={'content-type': 'image/jpeg'})
        print(json.loads(response.text))

    def send_gps(self, lng, lat):
        # img_encoded should already be encoded with cv2.imencode('.jpg', img)
        data = jsonpickle.encode({'lng': lng, 'lat': lat})
        response = requests.post('http://localhost:5000/api/gps', data=data, headers={'content-type': 'image/jpeg'})
        print(json.loads(response.text))

class CloudClient(Client):
    ### Works with AMS team's cloud server
    def __init__(self):
        # TODO
        pass

    def send_video_frame(self, img_encoded):
        # TODO
        pass

    def send_gps(self, lng, lat):
        # TODO
        pass


## TEST MAIN:
if __name__ == '__main__':
    # Sends image and gps coordinates using TestClient class to testserver.
    # testserver should be running.
    # When the image is sent, it returns its size in the response and saves it in black and white.
    # When the gps coordinates are sent, it returns them in the response.
    img = cv2.imread('test_img.jpg', 0)
    _, img_enc = cv2.imencode('.jpg', img)
    client = TestClient()
    client.send_video_frame(img_enc)
    client.send_gps(123.0, 456.0)