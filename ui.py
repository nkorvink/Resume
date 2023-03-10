# ui.py

# Starter code for assignment 2 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Nicholas Korvink
# nkorvik@uci.edu
# 39562903

import a4
import Profile
import sys

def ui():
    adminMode = False

    user = Profile.Profile()

    while True:
        userThing = input("Enter the information: ").split()

        if userThing[0] == "Q":
            a4.Q
        
        folderPath = userThing[1]

        if userThing[0] == "L":
            a4.L(folderPath, userThing)
        
        elif userThing[0] == "D":
            a4.D(folderPath)
        
        elif userThing[0] == "R":
            a4.R(folderPath)
        
        elif userThing[0] == "C" and "-n" in userThing:
            a4.C(folderPath, userThing, user)
        
        elif userThing[0] == "O":
            a4.O(userThing, user)
        
        elif userThing[0] == "E":
            a4.E(userThing, user)

        elif userThing[0] == "P":
            a4.P(userThing, user)

        else:
            print("Invalid input")

