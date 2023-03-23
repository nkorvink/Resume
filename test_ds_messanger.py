import ds_messenger
variable = ds_messenger.DirectMessenger("168.235.86.101", "nkorvink", "clown256")
variable.get_token()
variable.send("hello", "yakes")
for i in variable.retrieve_all():
    print(i.message)
