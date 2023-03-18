from ds_protocol import directmessage, decipher

def test():
    lst = []
    response = {"response": {"type": "ok", "message": "Direct message sent"}}
    messages = {"response": {"type": "ok", "messages": [{"message":"Hello User 1!", "from":"markb", "timestamp":"1603167689.3928561"}, {"message":"Bzzzzz", "from":"thebeemoviescript", "timestamp":"1603167689.3928561"}]}}
    y = decipher(response, messages, lst)
    print(y)

if __name__ == "__main__":
    test()
