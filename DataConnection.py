#  Copyright (c) 6/5/20, 1:52 AM.
#  Author 'Virgil Hoover'
#  License 'MIT License'

from mysql import connector


def mysql_query_read_connection(server='localhost', user='root', password='', query='') -> list:
    """ Read from a MySQL database and return the results """
    connection = connector.connect(server=server, username=user, password=password, readonly=True)
    results = connection.execute(connection.cmd_stmt_prepare(query))
    return results


if __name__ == '__main__':
    mysql_query_read_connection(server='', user='', password='', query='')
