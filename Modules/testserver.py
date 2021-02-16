from flask import Flask, request, Response
import json
import numpy as np
import cv2
import base64

num = 1
app = Flask(__name__)

@app.route('/api/gps', methods=['POST'])
def gps():
    # Test API endpoint that returns received gps coordinates
    data = json.loads(request.data)
    print(f'Received GPS coordinates: {data["lng"]}x{data["lat"]}\n')
    response = json.dumps({'message': f'Received GPS coordinates: {data["lng"]}x{data["lat"]}'})
    return Response(response=response, status=200, mimetype="application/json")


@app.route('/api/img', methods=['POST'])
def image():
    # Test API endpoint that simply saves image
    data = json.loads(request.data)
    jpg_original = base64.b64decode(data['img_encoded'])
    nparr = np.frombuffer(jpg_original, dtype=np.uint8)
    img = cv2.imdecode(nparr, flags=1)
    cv2.imwrite('test_output.jpg', img)

    print(f'Received image:')
    print(f'ID: {data["id"]}')
    print(f'Timestamp: {data["video_timestamp"]}')
    print(f'Channel: {data["channel"]}')
    print(f'Size: {img.shape[1]}x{img.shape[0]}')
    print(f'Image number: {data["img_num"]} of {data["total_num"]}')
    print(f'')

    response = json.dumps({'message': f'image received. size={img.shape[1]}x{img.shape[0]}'})
    return Response(response=response, status=200, mimetype="application/json")


@app.route('/api/sos', methods=['POST'])
def sos():
    # Handle SOS alert
    data = json.loads(request.data)
    print(f'Received SOS alert from ID={data["id"]}\n')
    response = json.dumps({'message': f'Received SOS alert from ID={data["id"]}'})
    return Response(response=response, status=200, mimetype="application/json")


@app.route('/api/lowbattery', methods=['POST'])
def lowbattery():
    # Handle low battery alert
    data = json.loads(request.data)
    print(f'Received low battery alert from ID={data["id"]}\n')
    response = json.dumps({'message': f'Received low battery alert from ID={data["id"]}'})
    return Response(response=response, status=200, mimetype="application/json")


@app.route('/api/alarm', methods=['GET', 'PUT'])
def alarm():
    # Handle alarm functionality
    data = json.loads(request.data)
    if request.method == 'GET':
        # Always return true
        print(f'Received alarm query from ID={data["id"]}\n')
        response = json.dumps({
            'message': f'Received alarm query from ID={data["id"]}',
            'ret_val': True
        })
        return Response(response=response, status=200, mimetype="application/json")
    elif request.method == 'PUT':
        # Clear flag and acknowledge
        print(f'Received alarm reset command from ID={data["id"]}\n')
        response = json.dumps({'message': f'Reset alarm flag for ID={data["id"]}'})
        return Response(response=response, status=200, mimetype="application/json")
    return Response(status=500)


@app.route('/api/allclear', methods=['GET', 'PUT'])
def allclear():
    # Handle alarm functionality
    data = json.loads(request.data)
    if request.method == 'GET':
        # Always return true
        print(f'Received all clear query from ID={data["id"]}\n')
        response = json.dumps({
            'message': f'Received all clear query from ID={data["id"]}',
            'ret_val': True
        })
        return Response(response=response, status=200, mimetype="application/json")
    elif request.method == 'PUT':
        # Clear flag and acknowledge
        print(f'Received all clear reset command from ID={data["id"]}\n')
        response = json.dumps({'message': f'Reset all clear flag for ID={data["id"]}'})
        return Response(response=response, status=200, mimetype="application/json")
    return Response(status=500)

if __name__ == "__main__":
    app.run(debug=True)
    