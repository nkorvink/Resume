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
            a4.Q_command
        
        folderPath = userThing[1]

        if userThing[0] == "L":
            a4.L_command(folderPath, userThing)
        
        elif userThing[0] == "D":
            a4.D_command(folderPath)
        
        elif userThing[0] == "R":
            a4.R_command(folderPath)
        
        elif userThing[0] == "C" and "-n" in userThing:
            a4.C_command(folderPath, userThing, user)
        
        elif userThing[0] == "O":
            folderPathExtra = folderPath
            a4.O_command(userThing, user)
        
        elif userThing[0] == "E":
            a4.E_command(userThing, user, folderPathExtra)

        elif userThing[0] == "P":
            a4.P_command(userThing, user)

        else:
            print("Invalid input")
