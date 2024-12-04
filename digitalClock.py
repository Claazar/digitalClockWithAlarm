# -*- coding: utf-8 -*-
# @Author: Buntschu Leonard
# @Date:   04-12-2024 09:35:55
# @Last Modified by:   Buntschu Leonard
# @Last Modified time: 04-12-2024 16:05:37

# DESCRIPTION:
# This code displays a digital clock using ASCII-Art onto the console.
# Additionally, you can set an alarm.
# The alarm sound is not mine. Full credits go to this youtube video: https://www.youtube.com/watch?v=o8sYXI7VHnY


#
# SETUP
#

import os
import time
from datetime import datetime
import pygame

# Define ASCII Art for digits 0-9 and colon (:)
ASCII_DIGITS = {
    '0': [
        "   ___    ",
        "  / _ \   ",
        " | | | |  ",
        " | | | |  ",
        " | |_| |  ",
        "  \___/   ",
    ],
    '1': [
        "    __    ",
        "   /_ |   ",
        "    | |   ",
        "    | |   ",
        "    | |   ",
        "    |_|   ",
    ],
    '2': [
        "   ___    ",
        "  |__ \   ",
        "     ) |  ",
        "    / /   ",
        "   / /_   ",
        "  |____|  ",
    ],
    '3': [
        "   ___    ",
        "  |___ \  ",
        "    __) | ",
        "   |__ <  ",
        "    __) | ",
        "  |____/  ",
    ],
    '4': [
        "  _  _     ",
        " | || |    ",
        " | || |_   ",
        " |__   _|  ",
        "    | |    ",
        "    |_|    ",
    ],
    '5': [
        "  _____    ",
        " | ____|   ",
        " | |__     ",
        " |___ \    ",
        "  ___) |   ",
        " |____/    ",
    ],
    '6': [
        "    __     ",
        "   / /     ",
        "  / /_     ",
        " | '_ \    ",
        " | (_) |   ",
        "  \___/    ",
    ],
    '7': [
        "  ______   ",
        " |____  |  ",
        "     / /   ",
        "    / /    ",
        "   / /     ",
        "  /_/      ",
    ],
    '8': [
        "   ___     ",
        "  / _ \    ",
        " | (_) |   ",
        "  > _ <    ",
        " | (_) |   ",
        "  \___/    ",
    ],
    '9': [
        "   ___     ",
        "  / _ \    ",
        " | (_) |   ",
        "  \__, |   ",
        "    / /    ",
        "   /_/     ",
    ],
    ':': [
        "           ",
        "    __     ",
        "   (__)    ",
        "    __     ",
        "   (__)    ",
        "           ",
    ],
}

# Gets the current time
def get_time(component):
    current_time = datetime.now()
    if component == "hours":
        return f"{current_time.hour:02}"
    elif component == "minutes":
        return f"{current_time.minute:02}"
    elif component == "seconds":
        return f"{current_time.second:02}"
    else:
        raise ValueError("Invalid component. Choose 'hours', 'minutes', or 'seconds'.")

# Builds the current time with the Ascii digits using the time from the get_time function
def asciiClock():
    hours = get_time("hours")
    htens, hones = hours[0], hours[1]

    minutes = get_time("minutes")
    mtens, mones = minutes[0], minutes[1]

    seconds = get_time("seconds")
    stens, sones = seconds[0], seconds[1]

    for i in range(6):  # Loop through each row of the ASCII representation
        print(
            ASCII_DIGITS[htens][i] + " " +
            ASCII_DIGITS[hones][i] + " " +
            ASCII_DIGITS[":"][i] + " " +
            ASCII_DIGITS[mtens][i] + " " +
            ASCII_DIGITS[mones][i] + " " +
            ASCII_DIGITS[":"][i] + " " +
            ASCII_DIGITS[stens][i] + " " +
            ASCII_DIGITS[sones][i]
        )

# Function to check if the current time matches the alarm time
def alarm_triggered(alarm_time):
    current_time = f"{get_time('hours')}:{get_time('minutes')}:{get_time('seconds')}"
    return current_time == alarm_time


#
# MAIN
#

# User chooses what to do
os.system("cls")
print("What would you like to do?")
print("1. View clock")
print("2. Set alarm")

wrongInput = "Please enter a valid integer corresponding to the possible selections!"


try: # If the input is not an integer, it will not be accepted and an error is printed
    choice = int(input(""))
except ValueError:
    raise ValueError(wrongInput)
# View clock
if choice == 1:
    showClock = True
    alarm_time = None  # No alarm set by default

    # Gets current second and saves it in a seperate variable
    seconds = get_time("seconds")
    stens, sones = seconds[0], seconds[1]

    currentSecond = sones


    while showClock:
        seconds = get_time("seconds")
        stens, sones = seconds[0], seconds[1]
        # When the second changes, the clock updates
        if currentSecond != sones:
            os.system("cls")
            asciiClock()
            currentSecond = sones


# Set alarm
elif choice == 2:
    # Set the alarm
    alarm_input = input("Enter alarm time (hh:mm:ss): ")
    try: # Makes sure that the entered time is in the correct Format
        parts = list(map(int, alarm_input.split(":")))
        if len(parts) == 3:
            alarm_time = f"{parts[0]:02}:{parts[1]:02}:{parts[2]:02}"
        else:
            raise ValueError
    except ValueError:
        print("Invalid alarm format. Use hh:mm:ss.")
        exit()

    # Start the clock with the alarm set
    showClock = True

    # Gets current second and saves it in a seperate variable
    seconds = get_time("seconds")
    stens, sones = seconds[0], seconds[1]

    currentSecond = sones

    while showClock:
        seconds = get_time("seconds")
        stens, sones = seconds[0], seconds[1]
        # When the second changes, the clock updates
        if currentSecond != sones:
            os.system("cls")
            asciiClock()
            currentSecond = sones

        # Check for alarm trigger
        if alarm_triggered(alarm_time):
            print("\n⏰ ALARM! Time's up! 🔔")
            showClock = False  # Stop the clock
            # Initialize mixer (to play the alarm sound)
            pygame.mixer.init()
            pygame.mixer.music.load("alarm.mp3")
            pygame.mixer.music.play(-1)  # -1 means loop indefinitely

            input("Alarm sound playing...Press Enter to snooze the timer...")
            pygame.mixer.music.stop()  # Stop the alarm


else: # Failsafe incase of missinputs
    print(wrongInput)


