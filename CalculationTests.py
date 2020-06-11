#  Copyright (c) 6/5/20, 1:47 AM.
#  Author 'Virgil Hoover'
#  License 'MIT License'

from datetime import datetime
from os import getenv
from os.path import join
from sys import platform, exit


def calculator() -> str:
    """ A quick calculator """
    print('(4480.5, 321, -4.3, -20.47, -22, -80, -1000, -5, & -178.98)')
    numbers = []
    flag = True
    st = 0
    if choice := input('Would you like the default configuration ').lower() == 'y':
        st = 8183.58
        numbers = [4480.5, 321, -4.3, -20.47, -22, -80, -1000, -5, -178.98]
        flag = True
    elif choice == 'n':
        st = float(input('Enter your starting number: '))
        is_finished = False
        while not is_finished:
            if number := float(input('Enter a number to add to the variance: ')) == 0:
                is_finished = True
            else:
                numbers.append(number)
        flag = False
    elif choice == 'x':
        exit(0)
    else:
        print('Invalid choice, please try again')
        exit(1)
    running_total = 0
    for i in numbers:
        running_total += i
    status = file_write(st, running_total, flag)
    return status


def file_write(st: int, running: int, is_auto: bool) -> str:
    """ File writing function called by the calculator function """
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if platform == 'linux':
        directory = f'{getenv("HOME")}/Desktop'
    elif platform == 'nt':
        directory = f'{getenv("UserProfile")}/Desktop'
    else:
        directory = './'
    filename = join(directory, 'calculations.txt')
    access_mode = 'a'
    try:
        with open(filename, access_mode) as file:
            file.write('\n<--' + str(timestamp) + '-->\n')
            if is_auto:
                file.write('<--Default Configuration-->\n')
            file.write('Your starting number is ' + str(st) + '\n')
            file.write('You entered numbers totaling ' + str(round(running, 2)) + '\n')
            file.write('You have ' + str(round(st - running, 2)) + ' remaining\n')
        status = 'Calculations Finished...\n'
    except IOError:
        status = 'There was a problem writing to the file'
    return status


if __name__ == '__main__':
    calculator()
