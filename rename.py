#/usr/bin/python3
from os import rename, listdir, chdir
from os.path import isfile, join


def renameFilesWithSearch(path, ext, start):
    chdir(path)
    onlyFiles = [item for item in listdir(path) if isfile(item)]
    for file in onlyFiles:
        if file[-4:] == ext and file[0:4] == start:
            name = file[:-4]
            finalName = name[0:-12] + ext
            rename(file, finalName)
            print('\n' + finalName, 'has been changed')
        else:
            print(file, 'has not been changed')


def renameWithoutSearch(path):
    chdir(path)
    onlyFiles = [item for item in listdir(path) if isfile(item)]
    for file in onlyFiles:
        ext = file[-4:]
        name = file[:-4]
        finalName = name[0:-12] + ext
        rename(file, finalName)
        print('\n' + finalName, 'has been changed')


def renameFile(path):
    chdir(path)
    newName = ''
    file = input('Please enter the filename to change: ')
    fileName = file[-4:]
    nameChunks = file[:-4].split()
    for item in nameChunks:
        newName += item.lower().capitalize() + ' '
    newName = newName[:-1] + file[-4:]
    rename(file, newName)
    print(file, 'has been renamed to', newName)


if __name__ == '__main__':
    p = input('Please enter the path to search: ')
    answer = int(input('Press 1 to rename a single file\n' \
                       'Press 2 to rename multiple files with a search\n' \
                       'Press 3 to rename multiple files\n'))
    if answer == 1:
        renameFile(p)
    elif answer == 2:
        x = input('Please enter the extension your searching for: ')
        s = input('Please enter the first four characters of the name: ')
        renameFilesWithSearch(p, x, s)
    elif answer == 3:
        renameWithoutSearch(p)
    else:
        print('Invalid Choice!')


