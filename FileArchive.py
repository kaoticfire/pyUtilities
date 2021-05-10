#  Copyright (c) 6/5/20, 1:41 AM.
#  Author 'Virgil Hoover'
#  License 'MIT License'

from shutil import make_archive
from zipfile import ZipFile, ZIP_LZMA

from requests import get

from ConsoleColor import ConsoleColor as Cc


def create_web_archive(web_url: str) -> list:
    web_data = get(web_url)
    with ZipFile('resources/archive.zip', 'ab', compression=ZIP_LZMA) as file_zip:
        file_zip.write(web_data.content)
    return file_zip.namelist()


def create_file_archive(file_name: str) -> list:
    with ZipFile('resources/archive.zip', mode='a', compression=ZIP_LZMA) as file_zip:
        file_zip.write(file_name)
    return file_zip.namelist()


def create_directory_archive(directory: str):
    return make_archive('resources/files', 'gztar', directory)


def extract_archive(file: str):
    try:
        with ZipFile(ZipFile(file), 'r') as file_reader:
            file_reader.namelist()
            choice = input('Do you wish to extract all the files or just one? (a/o) ')
            if choice.lower() == 'a':
                print(f'{Cc.WARNING}WARNING: Only do this if you trust the souce.')
                answer = input('Continue? ')
                if answer.lower() == 'y':
                    file_reader.extractall('files')
                else:
                    print(f'{Cc.WARNING}Operation aborted.')
                    exit(1)
            elif choice.lower() == 'o':
                needed_file = input('What file? ')
                file_reader.extract(needed_file)
    except FileNotFoundError:
        print(f'{Cc.FAIL}File not found, please check the path and try again!')
        exit(2)
        return False


if __name__ == '__main__':
    while True:
        file_to_use = input('Enter the file to work with: ')
        if file_to_use != '':
            print(create_file_archive(file_to_use))
        else:
            break
