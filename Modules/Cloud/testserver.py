## Credit: https://gist.github.com/kylehounslow/767fb72fde2ebdd010a0bf4242371594

from flask import Flask, request, Response
import jsonpickle
import json
import numpy as np
import cv2

num = 1
app = Flask(__name__)

@app.route('/api/img', methods=['POST'])
def image():
    # Test API endpoint that simply saves image
    global num
    r = request
    nparr = np.fromstring(r.data, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    cv2.imwrite(f'output{num}.jpg', img)
    num += 1

    # build a response dict to send back to client
    response = {'message': 'image received. size={}x{}'.format(img.shape[1], img.shape[0])
                }
    # encode response using jsonpickle
    response_pickled = jsonpickle.encode(response)

    return Response(response=response_pickled, status=200, mimetype="application/json")

@app.route('/api/gps', methods=['POST'])
def gps():
    # Test API endpoint that returns received gps coordinates
    r = request
    data = json.loads(r.data)

    # build a response dict to send back to client
    response = {'message': 'coordinates received={}x{}'.format(data['lng'], data['lat'])
                }
    # encode response using jsonpickle
    response_pickled = jsonpickle.encode(response)

    return Response(response=response_pickled, status=200, mimetype="application/json")


if __name__ == "__main__":
    app.run(debug=True)
    