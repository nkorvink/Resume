import ds_messenger

def main():
    variable = ds_messenger.DirectMessenger("168.235.86.101", "nkorvink", "clown256")
    variable.get_token()
    variable.send("i like blue", "spoods")
    lst = []
    for i in variable.retrieve_all():
        lst.append(i.message)
    assert len(lst) > 0

if __name__ == "__main__":
    main()
