import requests
import json
import cv2
import datetime
import base64
import config

class Client:
    def __init__(self, id):
        '''ID should be unique identifier (e.g., sim card), should be send with every request'''
        pass

    def send_gps(self, lng, lat):
        '''Request containing lattitude and longitude floats.'''
        pass

    def send_video_frame(self, channel, start_datetime, img_encoded, img_num, total_num, fps):
        '''Request sending a single frame from a video.
        A video is uniquely identified by its channel and its start time.
        channel: 0 (front camera) or 1 (back camera)
        start_datetime: when the first frame was captured (note: all frames of the same video should use the same value)
        img_encoded: .jpg image encoded using cv2.imencode()
        img_num: frame number in video (1 to img_total)
        total_num: total number of frames in the video
        fps: image caputure rate in frames per second
        '''
        pass

    def send_sos_warning(self):
        '''Request letting AMS know we received SOS button push'''
        pass

    def send_low_battery_warning(self):
        '''Request letting AMS know battery is low'''
        pass

    def query_play_alarm(self):
        '''Request to be used to periodically query if the user has selected to play the alarm sound
        after intrusion has been detected. Returns true or false.'''
        pass

    def query_all_clear(self):
        '''Request to be used to periodically query if the user has selected the all clear/ignore
        option after intrusion has been detected. Returns true or false.'''
        pass

    def query_send_video(self):
        '''Request to be used to periodically query if AMS or the user is requesting a 10 second video.'''
        pass

    def reset_play_alarm(self):
        '''Request to reset alarm flag on AMS side.'''
        pass

    def reset_all_clear(self):
        '''Request to reset all clear flag on AMS side.'''
        pass

    def reset_send_video(self):
        '''Request to reset send video flag on AMS side.'''
        pass


class TestClient(Client):
    ### Works with local test server
    def __init__(self, id):
        self.id = id

    def send_gps(self, lng, lat):
        data = json.dumps({
            'id': self.id,
            'lng': lng,
            'lat': lat
            })
        response = requests.post('http://localhost:5000/api/gps', data=data)
        print(json.loads(response.text))

    def send_video_frame(self, channel, start_datetime, img_encoded, img_num, total_num, fps):
        # Write .jpg ecoding as base64, then ascii
        img_as_txt = base64.b64encode(img_encoded).decode('ascii')
        data = json.dumps({
            'id': self.id,
            'channel': channel,
            'video_timestamp': start_datetime.strftime("%m/%d/%Y, %H:%M:%S"),
            'img_encoded': img_as_txt,
            'img_num': img_num,
            'total_num': total_num,
            'fps': fps
        })
        response = requests.post('http://localhost:5000/api/img', data=data)
        print(json.loads(response.text))
        

    def send_sos_warning(self):
        data = json.dumps({
            'id': self.id
        })
        response = requests.post('http://localhost:5000/api/sos', data=data)
        print(json.loads(response.text))

    def send_low_battery_warning(self):
        data = json.dumps({
            'id': self.id
        })
        response = requests.post('http://localhost:5000/api/lowbattery', data=data)
        print(json.loads(response.text))

    def query_play_alarm(self):
        data = json.dumps({
            'id': self.id
        })
        response = requests.get('http://localhost:5000/api/alarm', data=data)
        print(json.loads(response.text))
        return response.json()['ret_val']

    def query_all_clear(self):
        data = json.dumps({
            'id': self.id
        })
        response = requests.get('http://localhost:5000/api/allclear', data=data)
        print(json.loads(response.text))
        return response.json()['ret_val']

    def query_send_video(self):
        data = json.dumps({
            'id': self.id
        })
        response = requests.get('http://localhost:5000/api/sendvideo', data=data)
        print(json.loads(response.text))
        return response.json()['ret_val']

    def reset_play_alarm(self):
        data = json.dumps({
            'id': self.id
        })
        response = requests.put('http://localhost:5000/api/alarm', data=data)
        print(json.loads(response.text))

    def reset_all_clear(self):
        data = json.dumps({
            'id': self.id
        })
        response = requests.put('http://localhost:5000/api/allclear', data=data)
        print(json.loads(response.text))

class CloudClient(Client):
    ### Works with AMS team's cloud server
    def __init__(self):
        self.url = config.url
        self.key = config.key
        self.id = config.uid

    ### TODO: Populate with correct REST endpoint requests
    def send_gps(self, lng, lat):
        print('Attempting to send gps data')
        data = {
            'lat': lat,
            'long': lng
            }
        print(data)

        header = {'x-auth-token': self.key}

        print(header)
        print(f'{self.url}/vehicle/sendvideo')

        response = requests.put(f'{self.url}/vehicle/gps', data=data, headers=header)
        print('Received response:')
        print(json.loads(response.text))

    def send_video_frame(self, channel, start_datetime, img_encoded, img_num, total_num, fps):
        print(f'Attempting to send video frame {img_num}/{total_num}')
        img_as_txt = base64.b64encode(img_encoded).decode('ascii')
        img_as_txt = 'data:image/jpeg;base64,' + img_as_txt
        data = {
            'channel': channel,
            'video_timestamp': start_datetime.strftime("%m-%d-%Y, %H:%M:%S"),
            'img_num': img_num,
            'total_num': total_num,
            'fps': fps,
            'img_encoded': img_as_txt
        }
        #print(data)

        header = {'x-auth-token': self.key}

        response = requests.post(f'{self.url}/api/img', data=data, headers=header)
        print('Received response:')
        print(response)
        print(json.loads(response.text))

    def send_sos_warning(self):
        print('Attempting to send sos warning')
        data = {}
        print(data)

        header = {'x-auth-token': self.key}

        response = requests.post(f'{self.url}/sos/fromauto2u', data=data, headers=header)
        print('Received response:')
        print(json.loads(response.text))

    def send_low_battery_warning(self):
        print('Attempting to send low battery warning')
        header = {'x-auth-token': self.key}
        response = requests.put(f'{self.url}/api/lowbattery', headers=header)
        print('Received response:')
        print(json.loads(response.text))

    def query_play_alarm(self):
        print('Attempting to send alarm query')
        header = {'x-auth-token': self.key}
        response = requests.get(f'{self.url}/vehicle/playsound/{self.id}', headers=header)
        print('Received response:')
        print(response)
        print(json.loads(response.text))
        response = json.loads(response.text)
        return response['msg']

    def query_all_clear(self):
        print('Attempting to send all clear query')
        header = {'x-auth-token': self.key}
        response = requests.get(f'{self.url}/vehicle/allclear/{self.id}', headers=header)
        print('Received response:')
        print(json.loads(response.text))
        response = json.loads(response.text)
        return response['msg']

    def query_send_video(self):
        print('Attempting to send video request query')
        header = {'x-auth-token': self.key}
        response = requests.get(f'{self.url}/vehicle/sendvideo/{self.id}', headers=header)
        print('Received response:')
        print(json.loads(response.text))
        response = json.loads(response.text)
        return response['msg']

    def reset_play_alarm(self):
        print('Attempting to send reset alarm flag query')
        header = {'x-auth-token': self.key}
        response = requests.put(f'{self.url}/vehicle/playsound/{self.id}', headers=header)
        print('Received response:')
        print(json.loads(response.text))

    def reset_all_clear(self):
        print('Attempting to send reset all-clear flag query')
        header = {'x-auth-token': self.key}
        response = requests.put(f'{self.url}/vehicle/allclear/{self.id}', headers=header)
        print('Received response:')
        print(json.loads(response.text))

    def reset_send_video(self):
        print('Attempting to send send video flag query')
        header = {'x-auth-token': self.key}
        response = requests.put(f'{self.url}/vehicle/sendvideo/{self.id}', headers=header)
        print('Received response:')
        print(json.loads(response.text))


## TEST MAIN:
if __name__ == '__main__':
    # Test data transmission between client and server.
    # If using TestClient, testserver should be running.
    # If using CloudClient, AMS server should be running.
    client = CloudClient()

    # Test GPS coordinate transmission
    client.send_gps(987, 654)

    # Test image transmission with test_img.jpg
    img = cv2.imread('test_img.jpg', 1)
    _, img_enc = cv2.imencode('.jpg', img)
    time = datetime.datetime.now()
    num = 10
    for i in range(num):
        client.send_video_frame(0, time, img_enc, i, num, 1)
        client.send_video_frame(1, time, img_enc, i, num, 1)

    # # Test SOS
    client.send_sos_warning()

    # # Test alarm/sound
    client.query_play_alarm()
    client.reset_play_alarm()

    # # Test all-clear
    client.query_all_clear()
    client.reset_all_clear()

    # # Test video query
    client.query_send_video()
    client.reset_send_video()
    
