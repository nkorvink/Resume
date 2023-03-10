# a3.py

# Starter code for assignment 3 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Nicholas Korvink
# nkorvink@uci.edu
# 39562903

import os
import Profile
import sys
import ds_client
import ui
import OpenWeather
import LastFM

def recurring(path, userThing):
    for currentItem in os.listdir(path):
        fullPath = os.path.join(path, currentItem)
        if "-f" in userThing and os.path.isdir(fullPath):
            continue
        if "-s" in userThing and os.path.basename(fullPath) != userThing[-1]:
            continue
        if "-e" in userThing and os.path.splitext(fullPath)[1] != userThing[-1]:
            continue
        print(fullPath)
        if "-r" in userThing and os.path.isdir(fullPath):
            recurring(fullPath, userThing)

def recurringTwo(num, userThing, user):
    message = []
    for x in range(len(userThing) - 2):
        message.append(userThing[x + 2])
    if "-usr" == userThing[num]:
        user.username = userThing[num + 1]
    elif "-pwd" == userThing[num]:
        user.password = userThing[num + 1]
    elif "-bio" == userThing[num]:
        user.bio = userThing[num + 1]
    elif "-addpost" == userThing[num]:
        user.add_post = message
        answer = input("do you want this post sent to the internet? y/n only: ")
        if answer == "y":
            weather = OpenWeather.OpenWeather("92697", "US")
            weather.set_apikey("4d5a3718de2640c3ad57b4a198901c24")
            weather.load_data()

            music = LastFM.LastFM()
            music.set_apikey("107f1031947e3df0e1a30d5069c61368")
            music.load_data()

            for i in range(len(message)):
                if message[i] == "@weather":
                    message[i] = weather.description

                if message[i] == "@lastfm":
                    message[i] = music.topsongcount

            message = " ".join(message)
            server = user.dsuserver
            port = 3021
            username = user.username
            post = message
            password = user.password
            bio = user.bio
            ds_client.send(server, port, username, password, post, bio)
        elif answer == "n":
            pass
        else:
            print("bruh, follow instructions")
            exit
    elif "-delpost" == userThing[num]:
        user.del_post = userThing[num + 1]

    if num < len(userThing) - 1:
        recurringTwo(num + 1, userThing, user)

def recurringThree(num, userThing, user, post):
    if "-usr" in userThing:
        print(user.username)
    elif "-pwd" in userThing:
        print(user.password)
    elif "-bio" in userThing:
        print(user.bio)
    elif "-posts" in userThing:
        print(post)
    elif "-post" in userThing:
        print(post.get_entry(userThing[num + 1]))
    elif "-all" in userThing:
        print(user)
        print(post)

def Q():
    exit()

def L(folderPath, userThing):
    recurring(folderPath, userThing[2:])

def D(folderPath):
    print(folderPath + " DELETED")
    os.remove(folderPath)

def R(folderPath):
    if os.path.getsize(folderPath) == 0:
        print("EMPTY")
    else:
        with open(os.path.join(folderPath), "r") as fill:
            for line in fill:
                print(line)

def C(folderPath, userThing, user):
    with open(os.path.join(folderPath, userThing[-1] + ".dsu"), "w") as sumthing:
        pass
    idk = os.path.join(folderPath, userThing[-1] + ".dsu")
    user.dsuserver = input("Enter a server ip addy: ")
    user.username = input("Enter a username: ")
    user.password = input("Enter a password: ")
    x = input("do you want a bio, type y if you want to or anything else if you dont idgaf: ")
    if x == "y":
        user.bio = input("Enter a bio: ")
    user.save_profile(idk)

def O(userThing, user):
    user.load_profile(userThing[1])

def E(userThing, user):
    recurringTwo(1, userThing, user)

def P(userThing, user):
    post = Profile.Post()
    recurringThree(1, userThing, user, post)

def main():
    ui.ui

if __name__ == "__main__":
    main()