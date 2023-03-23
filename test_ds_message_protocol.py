import ds_protocol
import time

def main():
    variable = ds_protocol.directmessage("1234", "hello", "me",)
    assert variable == {"token":"1234", "directmessage": {"entry": "hello","recipient":"me", "timestamp": time.time()}}

if __name__ == "__main__":
    main()
