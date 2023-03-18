# Starter code for assignment 3 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Nicholas Korvink
# nkorvink@uci.edu
# 39562903

# The actual server can be found at the address 168.235.86.101 and port 3021
import ui
import socket
import ds_protocol
import json

def get_token(server:str, port:int, jon:dict):
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

def connection_to_server(server:str, port:int, jon:dict):
  if server != "168.235.86.101":
    return False

  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((server, port)) #connects to server
    x = json.dumps(jon)
    send = client.makefile("w") #able to read from the server
    send.write(x + "\r\n") #writes it to the server
    send.flush()
    send.close()

def send(server:str, port:int, username:str, password:str, message:str, bio:str=None):
  '''
  The send function joins a ds server and sends a message, bio, or both

  :param server: The ip address for the ICS 32 DS server.
  :param port: The port where the ICS 32 DS server is accepting connections.
  :param username: The user name to be assigned to the message.
  :param password: The password associated with the username.
  :param message: The message to be sent to the server.
  :param bio: Optional, a bio for the user.
  '''
  #TODO: return either True or False depending on results of required operation
  usr = ds_protocol.join(username, password)
  token = get_token(server, port, usr)
  this = ds_protocol.bio(token, bio) #sets bio and token information to json format
  connection_to_server(server, port, this)
  works = ds_protocol.post(token, message) #sets post and token information to json format
  connection_to_server(server, port, works)
  return True

def send_message(server:str, port:int, message:str, recipient:str, username:str, password:str):
  usr = ds_protocol.join(username, password)
  token = get_token(server, port, usr)
  entry = ds_protocol.directmessage(token, message, recipient)
  connection_to_server(server, port, entry[0])
  connection_to_server(server, port, entry[1])
  return True