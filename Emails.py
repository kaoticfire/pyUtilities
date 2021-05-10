#  Copyright (c) 6/5/20, 1:44 AM.
#  Author 'Virgil Hoover'
#  License 'MIT License'
from csv import reader


def get_email(key: str, file) -> str:
    """ Find an SMS Gateway for emails """
    with open(file, newline='') as cf:
        email_sms = {rows[0]: rows[1] for rows in reader(cf, delimiter=',')}
    if key in email_sms:
        return email_sms[key]
    else:
        return 'Not Found'


if __name__ == '__main__':
    print('Find the Email SMS Gateway address')
    csv_file = 'resources/providers.csv'
    suffix = get_email(key=input('What is the cell provider? '), file=csv_file)
    if suffix == 'Not Found':
        print('Provider does not support this feature.')
    else:
        print('\nThe email address to use is:\n', input('What is the 10 digit cell number? ') + suffix)