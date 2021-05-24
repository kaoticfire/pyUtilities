# /usr/bin/python3
from os import rename, listdir, chdir, path
from os.path import isfile


def rename_files_with_search(loc):
    ext = input('Please enter the extension your searching for: ')
    start = input('Please enter the first four characters of the name: ')

    only_files = [item for item in listdir(loc) if isfile(item)]
    for file in only_files:
        if file[-4:] == ext and file[0:4] == start:
            name = file[:-4]
            final_name = name[0:-12] + ext
            rename(file, final_name)
            print('\n' + final_name, 'has been changed')
        else:
            print(file, 'has not been changed')


def rename_with_search_pattern(loc):
    old_term = input('Please enter the search term to remove: ')
    new_term = input('Please enter the new term to use: ')
    _counter = 0
    for file in listdir(loc):
        if file.find(old_term) > -1:
            _counter += 1
            rename(path.join(loc, file), path.join(loc, file.replace(old_term, new_term)))
    if _counter == 0:
        print("No file has been found")


def rename_without_search(loc):
    only_files = [item for item in listdir(loc) if isfile(item)]
    for file in only_files:
        ext = file[-4:]
        name = file[:-4]
        final_name = name[0:-12] + ext
        rename(file, final_name)
        print('\n' + final_name, 'has been changed')


def fix_file_name(loc):
    only_files = [item for item in listdir(loc) if isfile(item)]
    for file in only_files:
        ext = file[-3:]
        name = file[:-4]
        final_name = name[0:-1] + '.w' + ext
        rename(file, final_name)
        print(final_name, 'has been changed\n')


def rename_file():
    new_name = ''
    file = input('Please enter the filename to change: ')
    for item in file[:-4].split():
        new_name += item.lower().capitalize() + ' '
    new_name = new_name[:-1] + file[-4:]
    rename(file, new_name)
    print(file, 'has been renamed to', new_name)


if __name__ == '__main__':
    p = input('Please enter the path to search: ')
    chdir(p)
    answer = int(input('Press 1 to rename a single file\n'
                       'Press 2 to rename multiple files with a search\n'
                       'Press 3 to rename multiple files\n'
                       'Press 4 to fix file names\n'
                       'Press 5 to define search term for file rename\n'))
    if answer == 1:
        rename_file()
    elif answer == 2:
        rename_files_with_search(p)
    elif answer == 3:
        rename_without_search(p)
    elif answer == 4:
        fix_file_name(p)
    elif answer == 5:
        rename_with_search_pattern(p)
    else:
        print('Invalid Choice!')
