#  Copyright (c) 6/5/20, 1:07 PM.
#  Author 'Virgil Hoover'
#  License 'MIT License'

from array import array
from locale import setlocale, LC_ALL
from os import system
from random import choice, shuffle, randint
from string import ascii_uppercase, ascii_lowercase, digits, punctuation
from sys import platform

from enchant import Dict


# Password Sources found in resources/main.json


def password_generator(length: int) -> str:
    """ Generates a password of n length, comprised of letters (upper and lower), numbers, and symbols. """
    generated_password = ''
    temporary_list = ''
    combined_list = digits + ascii_uppercase + ascii_lowercase + punctuation
    random_digit = choice(digits)
    random_upper = choice(ascii_uppercase)
    random_lower = choice(ascii_lowercase)
    random_symbol = choice(punctuation)
    temporary_password = random_digit + random_upper + random_lower + random_symbol
    print('\n\nCreating a password at least', length, 'characters long.')
    for _ in range(randint(length, 32) - len(temporary_password)):
        temporary_password += choice(combined_list)
        temporary_list = array('u', temporary_password)
        shuffle(temporary_list)

    for item in temporary_list:
        generated_password += item

    return generated_password


def check_if_password_found(password: str) -> bool:
    """ Compares a given password to a list of hacked or easily hackable passwords. """
    password_string = ''
    password_list = []
    file = 'resources/passwords.txt'

    with open(file, 'r') as file_reader:
        password_list.append(file_reader.read())

    for item in password_list:
        password_string += item

    if (password not in password_string) and (not dictionary_check(password)):
        with open(file, 'a') as file_writer:
            file_writer.write(password_string)
        return False
    else:
        return True


def dictionary_check(password: str) -> bool:
    dictionary_string = Dict('en_US')
    setlocale(LC_ALL, 'en_US.UTF-8')
    return dictionary_string.check(password)


def clear_screen():
    if platform == 'linux':
        system('clear')
    elif platform == 'nt':
        system('cls')


if __name__ == '__main__':
    print('''Password Checker / Generator
    1. Check a password
    2. Generate a password''')
    menu_choice = int(input('Which would you like to do? '))

    if menu_choice == 1:
        string_password = input('Please enter the password to check. ')
        if check_if_password_found(password=string_password):
            print('The password has been already listed and is not safe to use.')
            if input('Would you like to have one created for you? ').lower() == 'y':
                print('Your new password is', password_generator(length=int(input('How long do you need it to be? '))))
        else:
            print('The password is safe at this time.')
    elif menu_choice == 2:
        print('Your new password is:\n', password_generator(length=int(input('How long do you need it to be? '))))
    else:
        print('Invalid Choice!!!')
        exit(1)
