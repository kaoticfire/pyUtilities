# /usr/bin/python3
# Copyright (c) July 25th, 2020
# Modified: October 31st, 2020
# License: MIT
#
# A Script to simulate user interaction that will disable the screen
# from going to sleep and activating screen saver as well as tricking
# Skype into thinking the user is still present

__author__ = 'Virgil Hoover'
__version__ = '1.3.0'
__name__ = 'Sys Key'

# See change log file for versions and list of changes

from datetime import datetime
from time import sleep
from logging import getLogger, basicConfig, Formatter, INFO
from logging.handlers import RotatingFileHandler
from os import system, getenv
import webbrowser

CYAN = '\033[1;36;40m'
RED = '\033[1;31;40m'
GREEN = '\033[1;32;40m'
YELLOW = '\033[1;33;40m'
BLUE = '\033[1;34;40m'
MAGENTA = '\033[0;35;40m'


def user_simulation(current):
    """ This function simulates the user interaction"""
    # Import modules specific to this function
    from pyautogui import press
    from random import randint
    from sys import platform, stdout, exit as xt

    # Set some variables like window size, the key used, & a counter.
    # TODO: Fix bug with linux terminal resizing
    system('mode con: cols=40 lines=7')
    sim_key = 'f4'
    key_press_count = 0
    total_duration = 0

    # Perform user interaction until canceled by user
    try:
        while True:
            if time_range(current):
                xt(0)

            # Clear the screen and set tile depending on OS
            if platform == 'win32':
                system('title' + __name__)
                system('cls')
            else:
                print('\033]0;' + __name__ + '\a', end='')
                system('clear')

            # Format consol output with color
            print(GREEN, '** User Input Simulation **\n',
                  YELLOW, '** Press Ctrl + C to quit **')

            random_duration = randint(1, 4) * 60
            time_duration = int(random_duration / 60)
            press(sim_key)
            key_press_count += 1
            tense = ''

            # Check if first iteration and give correct tense
            if key_press_count < 2:
                tense = 'time'
            else:
                tense = 'times'

            print(CYAN, str(time_duration), RED + 'minute interval\n',
                  CYAN, sim_key, RED + 'has been pressed',
                  CYAN + str(key_press_count), RED + tense)
            print(RED, 'For a total time of',
                  CYAN + str(convert_time(total_duration)))
            total_duration += random_duration
            countdown(random_duration)

    except KeyboardInterrupt:
        # Listen for the user to quit program
        return str(convert_time(total_duration))


def convert_time(seconds):
    seconds = seconds % (24 * 3600)
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return '{:02d}:{:02d}'.format(hours, minutes)


def countdown(t):
    while t:
        tf = '\033[1;36;40m {:02d}:{:02d}\033[1;31;40m currently remaining'.format(*divmod(t, 60))
        print(tf, end='\r')
        sleep(1)
        t -= 1


def time_range(time_compare):
    """ Return true if x is in range [start, end]"""
    start = datetime.strptime('05:00', '%H:%M')
    end = datetime.strptime('17:00', '%H:%M')

    if start >= time_compare >= end:
        return True
    else:
        return False


if __name__ == 'Sys Key':
    ACCESS = 'a'
    # 1kb = 1*1024, 1mb = 1*1024*1024, 1gb = 1*1024*1024*1024
    SIZE = 5 * 1024 * 1024
    now = datetime.now()
    total = user_simulation(now)
    basicConfig(level=INFO)
    FILE = getenv('HOME') + '/time.log'
    fileHandler = RotatingFileHandler(FILE, ACCESS, maxBytes=SIZE,
                                      backupCount=1, encoding=None, delay=0)
    fileFormat = Formatter('%(asctime)s - %(levelname)s - %(message)s',
                           datefmt='%Y-%m-%d %H:%M:%S')
    fileHandler.setLevel(INFO)
    fileHandler.setFormatter(fileFormat)
    logger = getLogger(__name__)
    logger.addHandler(fileHandler)
    logger.info(total)
    sleep(1)
    webbrowser.open(FILE)
