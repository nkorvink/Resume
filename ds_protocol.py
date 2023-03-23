# ds_protocol.py

# Starter code for assignment 3 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Nicholas Korvink
# nkorvink@uci.edu
# 39562903

import json
from collections import namedtuple
import time
# Namedtuple to hold the values retrieved from json messages.
# TODO: update this named tuple to use DSP protocol keys
DataTuple = namedtuple('DataTuple', ['message', 'token', 'type'])


def join(username, password):
    x = {"join": {"username": username, "password": password, "token": ""}}
    return x


def post(token, post):
    x = {"token": token, "post": {"entry": post, "timestamp": time.time()}}
    return x


def bio(token, bio):
    x = {"token": token, "bio": {"entry": bio, "timestamp": time.time()}}
    return x


def extract_json(json_msg) -> DataTuple:
    '''
    Call the json.loads function on a json string and convert it to a DataTuple object
    '''
    try:
        json_obj = json.loads(json_msg)
        typ = json_obj["response"]["type"]
        msg = json_obj["response"]["message"]
        token = json_obj["response"]["token"]
    except json.JSONDecodeError:
        print("Json cannot be decoded.")

    return DataTuple(msg, token, typ)


def directmessage(user_token, entry, recipient, que=None):
    message = {}
    if que is None:
        message = {"token": user_token, "directmessage": {"entry": entry, "recipient": recipient, "timestamp": time.time()}}
    elif que == "all":
        message = {"token": user_token, "directmessage": "all"}
    elif que == "new":
        message = {"token": user_token, "directmessage": "new"}
    return message


def decipher(messages, lst):
    messages = json.loads(messages)
    for i in messages["response"]["messages"]:
        lst.append(i)
    return lst
