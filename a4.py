# a3.py

# Starter code for assignment 3 in ICS 32 Programming with Software Libraries

# Replace the following placeholders with your information.

# Nicholas Korvink
# nkorvink@uci.edu
# 39562903

import os
import ds_client
import ui
from OpenWeather import OpenWeather
from LastFM import LastFM

def test(message:str):
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
    return message

def recurring(path, userThing):
    for currentItem in os.listdir(path):
        fullPath = os.path.join(path, currentItem)
        if "-f" in userThing and os.path.isdir(fullPath):
            continue
        if "-s" in userThing and os.path.basename(
        fullPath) != userThing[-1]:
            continue
        if "-e" in userThing and os.path.splitext(
        fullPath)[1] != userThing[-1]:
            continue
        print(fullPath)
        if "-r" in userThing and os.path.isdir(fullPath):
            recurring(fullPath, userThing)


def recurringTwo(num, userThing, user, folderPathExtra):
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
        message = " ".join(message)
        user.add_post(message)
        answer = input(
        "do you want this post sent to the internet? y/n only: ")
        if answer == "y":
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
            server = user.dsuserver
            port = 3021
            username = user.username
            post = message
            password = user.password
            bio = user.bio
            ds_client.send(
            server, port, username, password, post, bio)
        elif answer == "n":
            pass
        else:
            print("bruh, follow instructions")
            exit
    elif "-delpost" == userThing[num]:
        user.del_post = userThing[num + 1]
    if num < len(userThing) - 1:
        recurringTwo(num + 1, userThing, user, folderPathExtra)
        user.save_profile(folderPathExtra)


def recurringThree(num, userThing, user):
    if "-usr" in userThing:
        print(user.username)
    elif "-pwd" in userThing:
        print(user.password)
    elif "-bio" in userThing:
        print(user.bio)
    elif "-posts" in userThing:
        for i in user._posts:
            print(i)
    elif "-post" in userThing:
        print(user._posts.get_entry(userThing[num + 1]))
    elif "-all" in userThing:
        print(user)
        print(user._posts)


def Q_command():
    exit()


def L_command(folderPath, userThing):
    recurring(folderPath, userThing[2:])


def D_command(folderPath):
    print(folderPath + " DELETED")
    os.remove(folderPath)


def R_command(folderPath):
    if os.path.getsize(folderPath) == 0:
        print("EMPTY")
    else:
        with open(os.path.join(
            folderPath), "r") as fill:
            for line in fill:
                print(line)


def C_command(folderPath, userThing, user):
    with open(os.path.join(
    folderPath, userThing[-1] + ".dsu"), "w") as sumthing:
        pass
    idk = os.path.join(folderPath, userThing[-1] + ".dsu")
    user.dsuserver = input("Enter a server ip addy: ")
    user.username = input("Enter a username: ")
    user.password = input("Enter a password: ")
    x = input(
    "do you want a bio, type y if you want to or anything else if you dont: ")
    if x == "y":
        user.bio = input("Enter a bio: ")
    user.save_profile(idk)


def O_command(userThing, user):
    user.load_profile(userThing[1])


def E_command(userThing, user, folderPathExtra):
    recurringTwo(1, userThing, user, folderPathExtra)


def P_command(userThing, user):
    recurringThree(1, userThing, user)


def main():
    ui.ui()


if __name__ == "__main__":
    print("Hello, and welcome to the UI")
    print("Some example commands to run are: ")
    print("1. 'C [folder path] -n [file name]' will create a file with the specified name at the desired location.")
    print("2. 'O [file path]' will load a already created user")
    print("3. 'L [folder path]' will print the contents of the specified folder")
    print("4. 'R [file path]' will show what is in the file")
    print("5. 'D [file path]' will delete the specified folder")
    print("6. 'E [command] [info]' will take a alredy loaded user and add the information to a location based on the command given.")
    print("Commands include: -usr, -pwd, -bio, -addpost, -delpost")
    print("7. 'P [command]' will print the specified command of the loaded user")
    print("Commands include: -usr, -pwd, -bio, -posts, -post [ID#], -all")
    print("8. 'Q' quits the program")
    main()
