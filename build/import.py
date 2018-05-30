#!/usr/bin/env python3

import getpass
import json
import os
import pymysql
import subprocess
import sys
import time

terminal_width = os.get_terminal_size().columns


def throw_error(message, detailed=None):
    print('Error: {0}'.format(message))


def report_status(message, has_status=False, status=True, display_dots=True):
    global terminal_width

    if has_status:
        print(message + '... ' + str('OK' if status else 'FAILED').rjust(terminal_width - (len(message) + 5)))
    elif display_dots:
        print(message + '...')
    else:
        print(message)


def request_confirmation(message, default='y'):
    while True:
        print('{0} [{1}/{2}]'.format(message, 'Y' if default is 'y' else 'y', 'N' if default is 'n' else 'n'), end=' ')
        key = input().lower()

        if key in ('y', 'n', 'yes', 'no'):
            return key != 'n' and key != 'no'

        elif not key:
            return default == 'y'

        print('Error: Invalid input')


def request_information(message, minlength=0, maxlength=25, hide=False, default=None):
    if default:
        message = '{0} (default: {1}): '.format(message, default)
    else:
        message = '{0}: '.format(message)

    while True:
        if not hide:
            print(message, end='')
            inpt = input()
        else:
            inpt = getpass.getpass(prompt=message)

        if len(inpt) in range(minlength, maxlength + 1) or default:
            return inpt if inpt else default

        print('Invalid input. Input should be between {0} and {1} characters'.format(minlength, maxlength))


def import_tables(cursor, wiki_info):
    statements = []

    result = True
    try:
        with open('data.sql') as file:
            current_statement = ''

            for line in file:
                clean_line = line.strip()
                line = line.replace('{db_prefix}', db_pref)

                for key, value in wiki_info.items():
                    line = line.replace('{' + 'data:{0}'.format(key) + '}', value)

                if clean_line.startswith('--') or not clean_line:
                    continue

                if clean_line.endswith(';'):
                    statements.append(current_statement + line)
                    current_statement = ''
                else:
                    current_statement += line

            if current_statement:
                statements.append(current_statement)
                current_statement = ''

        for statement in statements:
            cursor.execute(statement)

        statements = []

    except Exception as e:
        result = False
        throw_error('Could not import data.', e)
        return

    except IOError as e:
        result = False
        print('Could not open .sql file')
        return

    finally:
        report_status('Importing data', True, result)

    return True


class Connection:
    def __init__(self, server, username, password, dbname):
        self.server = server
        self.username = username
        self.password = password
        self.dbname = dbname

    def connect(self):
        result = True
        try:
            self.connection = pymysql.connect(host=self.server, user=self.username, password=self.password, db=self.dbname)
            self.cursor = self.connection.cursor()

        except Exception as e:
            result = False
            throw_error('Could not connect to database', e)

        finally:
            report_status('Establishing database connection', True, result)

        return result

    def close():
        result = True
        try:
            self.connection.close()
            self.cursor.close()

        except Exception as e:
            result = False

            throw_error('Could not close database connection', e)

        finally:
            report_status('Closing database connection', True, result)

        return result


def run():
    print(':: HiLang command line installer')

    print('Welcome to HiLang!')

    if not request_confirmation('This script will install HiLang. Do you wish to proceed?'):
        report_status('Aborting')
        return

    print(':: Database server information')

    if request_confirmation('Should new tables be created?'):
        while True:
            info_host = request_information('Host', default='localhost')
            info_username = request_information('Username', default='root')
            info_password = request_information('Password', minlength=5, hide=True)
            info_dbname = request_information('Database name', default='hilang')

            connection = Connection(info_host, info_username, info_password, info_dbname)

            if connection.connect():
                break

            print('Could not connect to database. Please try again')

        print('Database connection established')

        if not import_tables(connection.cursor, {}):
            return

    else:
        report_status('Aborting')
        return

    print(':: Create root account')
    try:
        subprocess.run((('python3' if sys.platform is 'posix' else 'python') + ' ../manage.py createsuperuser').split())

    except subprocess.CalledProcessError as e:
        throw_error('Could not create super user', e)

    print('Thank you for installing HiLang. The installation is now complete.')


if __name__ == '__main__':
    try:
        run()

    except KeyboardInterrupt:
        report_status('\nAborting')
