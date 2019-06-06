#!/usr/bin/env python3

import bcrypt
from getpass import getpass as password_input
import json
from os import path, urandom

DEFAULT_LOCATION = path.expanduser('~/userdata.json')


def load_users(location):
    with open(location, 'r') as f:
        return json.load(f)


def save_users(location, user_list):
    with open(location, 'w') as f:
        json.dump(user_list, f)


def add_user_to_list(user_list, username, password):
    already_exists = False
    for u in user_list:
        if u['username'] == username:
            already_exists = True
            print("Username '{}' already exists".format(username))
            break
    if not already_exists:
        hashed_pw = bcrypt.hashpw(bytes(password, 'utf-8'),
                                  bcrypt.gensalt()).decode('utf-8')
        user_list.append({'username': username, 'password_hash': hashed_pw})


def main():
    user_db = []
    if path.exists(DEFAULT_LOCATION):
        user_db = load_users(DEFAULT_LOCATION)

    for u in user_db:
        print(u['username'])

    new_username = input('New User: ')
    new_password = password_input('Password for {}: '.format(new_username))

    add_user_to_list(user_db, new_username, new_password)
    save_users(DEFAULT_LOCATION, user_db)


if __name__ == '__main__':
    main()
