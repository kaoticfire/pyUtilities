#/usr/bin/python3
from os import rename, listdir, chdir, path
from os.path import isfile


def renameFilesWithSearch(p, ext, start):
    chdir(p)
    onlyFiles = [item for item in listdir(p) if isfile(item)]
    for file in onlyFiles:
        if file[-4:] == ext and file[0:4] == start:
            name = file[:-4]
            finalName = name[0:-12] + ext
            rename(file, finalName)
            print('\n' + finalName, 'has been changed')
        else:
            print(file, 'has not been changed')


def renameWithSearchPattern(p, old_term, new_term):
    chdir(p)
    counter = 0
    for file in listdir(p):
        if file.find(old_term) > -1:
            counter += 1
            rename(path.join(p, file), path.join(p, file.replace(old_term, new_term)))
    if counter == 0:
        print("No file has been found")


def renameWithoutSearch(p):
    chdir(p)
    onlyFiles = [item for item in listdir(p) if isfile(item)]
    for file in onlyFiles:
        ext = file[-4:]
        name = file[:-4]
        finalName = name[0:-12] + ext
        rename(file, finalName)
        print('\n' + finalName, 'has been changed')


def fixFileName(p):
    chdir(p)
    onlyFiles = [item for item in listdir(p) if isfile(item)]
    for file in onlyFiles:
        ext = file[-3:]
        name = file[:-4]
        finalName = name[0:-1] + '.w' + ext
        rename(file, finalName)
        print(finalName, 'has been changed\n')


def renameFile(p):
    chdir(p)
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
    answer = int(input('Press 1 to rename a single file\n'
                       'Press 2 to rename multiple files with a search\n'
                       'Press 3 to rename multiple files\n'
                       'Press 4 to fix file names\n'
                       'Press 5 to define search term for file rename\n'))
    if answer == 1:
        renameFile(p)
    elif answer == 2:
        x = input('Please enter the extension your searching for: ')
        s = input('Please enter the first four characters of the name: ')
        renameFilesWithSearch(p, x, s)
    elif answer == 3:
        renameWithoutSearch(p)
    elif answer == 4:
        fixFileName(p)
    elif answer == 5:
        o = input('Please enter the search term to remove: ')
        n = input('Please enter the new term to use: ')
        renameWithSearchPattern(p, o, n)
    else:
        print('Invalid Choice!')
