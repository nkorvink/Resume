import socket
import json
import time
import ds_protocol
from LastFM import LastFM
from OpenWeather import OpenWeather


class DirectMessage:
    def __init__(self):
        self.recipient = None
        self.message = None
        self.timestamp = None


class DirectMessenger:
    def __init__(self, dsuserver=None, username=None, password=None):
        self.dsuserver = dsuserver
        self.username = username
        self.password = password
        self.token = None

    def send(self, message:str, recipient:str) -> bool:
        # TODO must return true if message successfully sent, false if send failed.
        weather = OpenWeather()
        weather.set_apikey(
        "4d5a3718de2640c3ad57b4a198901c24")
        weather.load_data()
        message = weather.transclude(message)
        music = LastFM()
        music.set_apikey(
        "107f1031947e3df0e1a30d5069c61368")
        music.load_data()
        message = music.transclude(message)
        try:
            entry = ds_protocol.directmessage(self.token, message, recipient)
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
                client.connect((self.dsuserver, 3021)) #connects to server
                x = json.dumps(entry)
                send = client.makefile("w") #able to read from the server
                send.write(x + "\r\n") #writes it to the server
                send.flush()
                send.close()
            return True
        except:
            return False

    def retrieve_new(self) -> list:

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect((self.dsuserver, 3021)) #connects to server
            x = json.dumps(ds_protocol.directmessage(self.token, "message", "recipient", "new"))
            send = client.makefile("w") #able to read from the server
            send.write(x + "\r\n") #writes it to the server
            send.flush()
            send.close()
            recv = client.makefile("r")
            hi = recv.readline()[:-1] #reads server message
            recv.close()
            data = ds_protocol.decipher(hi, []) #gets data tuple from extract json
            lst = []
            for i in data:
                dm = DirectMessage()
                dm.recipient = i["from"]
                dm.message = i["message"]
                dm.timestamp = i["timestamp"]
                lst.append(dm)
            return lst

    def retrieve_all(self) -> list:

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect((self.dsuserver, 3021)) #connects to server
            x = json.dumps(ds_protocol.directmessage(self.token, "message", "recipient", "all"))
            send = client.makefile("w") #able to read from the server
            send.write(x + "\r\n") #writes it to the server
            send.flush()
            send.close()
            recv = client.makefile("r")
            hi = recv.readline()[:-1] #reads server message
            recv.close()
            data = ds_protocol.decipher(hi, []) #gets data tuple from extract json
            lst = []
            for i in data:
                dm = DirectMessage()
                dm.recipient = i["from"]
                dm.message = i["message"]
                dm.timestamp = i["timestamp"]
                lst.append(dm)
            return lst

    def get_token(self):
        if self.dsuserver != "168.235.86.101":
            return False

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect((self.dsuserver, 3021)) #connects to server
            x = json.dumps(ds_protocol.join(self.username, self.password))
            send = client.makefile("w") #able to read from the server
            send.write(x + "\r\n") #writes it to the server
            send.flush()
            send.close()
            recv = client.makefile("r")
            hi = recv.readline()[:-1] #reads server message
            recv.close()
            data = ds_protocol.extract_json(hi) #gets data tuple from extract json
            token = data[1] #gets token from tuple
            self.token =  token
