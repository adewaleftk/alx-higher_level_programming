#!/usr/bin/python3

import requests
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]

    url = f'https://api.github.com/users/{username}'
    response = requests.get(url, auth=(username, password))

    if response.status_code == 200:
        data = response.json()
        print(f'Your user ID is: {data["id"]}')
    else:
        print(f'Error: {response.status_code}')

