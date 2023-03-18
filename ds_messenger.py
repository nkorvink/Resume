import socket
import json
import time
import ds_client

class DirectMessage:
    def __init__(self):
        self.recipient = None
        self.message = None
        self.timestamp = None


class DirectMessenger:
    def __init__(self, dsuserver=None, username=None, password=None):
        self.token = None
		
    def send(self, message:str, recipient:str) -> bool:
        # TODO must return true if message successfully sent, false if send failed.
        try:
            ds_client.send_message("168.235.86.101", 3021, message, recipient, "nkorvink", "clown256")
        except:
            return False
		
    def retrieve_new(self) -> list:
        if server != "168.235.86.101":
            return False

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect((server, port)) #connects to server
            x = json.dumps(jon)
            send = client.makefile("w") #able to read from the server
            send.write(x + "\r\n") #writes it to the server
            send.flush()
            send.close()
            recv = client.makefile("r")
            hi = recv.readline()[:-1] #reads server message
            recv.close()
            data = ds_protocol.extract_json(hi) #gets data tuple from extract json
            token = data[1] #gets token from tuple
            return token

    def retrieve_all(self) -> list:
        if server != "168.235.86.101":
            return False

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect((server, port)) #connects to server
            x = json.dumps(jon)
            send = client.makefile("w") #able to read from the server
            send.write(x + "\r\n") #writes it to the server
            send.flush()
            send.close()
            recv = client.makefile("r")
            hi = recv.readline()[:-1] #reads server message
            recv.close()
            data = ds_protocol.extract_json(hi) #gets data tuple from extract json
            token = data[1] #gets token from tuple
            return token