#  Copyright (c) 6/5/20, 1:07 PM.
#  Author 'Virgil Hoover'
#  License 'MIT License'
from json import load

from bs4 import BeautifulSoup
from requests import get

from ConsoleColor import ConsoleColor as Cc


def version_finder(web_url: str, file: str) -> str:
    """ This function finds the latest version and then compares it to that found in a json file. """
    # Create some variables
    soup = BeautifulSoup(get(web_url).text, 'lxml')
    table_rows = soup.find('div', {'id': 'tableWraper'}).find('tbody').find_all('tr')
    data = []
    for tr in table_rows:
        data.append([i.text for i in tr.find_all('td')])
    data.remove([])
    data_list = [item for sub_list in data for item in sub_list]

    # Read Json file
    with open(file, 'r') as json_reader:
        json_data = load(json_reader)
        current_mod = json_data['Model_Name']
        current_ver = json_data['Current_Version']

    # Parse web data
    model_res = list(filter(lambda x: current_mod in x, data_list))
    if current_mod in str(model_res):
        model_results = current_mod
    else:
        model_results = model_res
    version_results = str(list(filter(lambda x: current_ver in x, data_list))[0])

    # Compare found to given
    if model_results == current_mod:
        if version_results == current_ver:
            return f'{Cc.SUCCESS}Your {current_mod} is running the most up to date version.'
        else:
            return f'{Cc.WARNING}The most recent version is {version_results},' \
                   f' but your {current_mod} is running {current_ver}'
    else:
        return f'{Cc.FAIL}Your {current_mod} is not the same as the {model_results} that you searched for.'


if __name__ == '__main__':
    url = 'https://support.apple.com/en-us/HT201222'
    json_file = 'resources/main.json'
    try:
        print(f'{Cc.BOLD}' + version_finder(web_url=url, file=json_file))
    except AttributeError:
        print('Double cheeck your URL and try again.')
