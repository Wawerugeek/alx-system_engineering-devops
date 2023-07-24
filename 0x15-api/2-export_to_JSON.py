#!/usr/bin/python3
"""READS DATA FROM API AND stores the data"""
import json
import requests
import sys


def main():
    """This script reads data from a Fake API and
    stores the infomation in a JSON file
    """
    USER_ID = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(USER_ID)
    tasks_url = ("https://jsonplaceholder.typicode.com/users/{}/todos".
                 format(USER_ID))
    tasks = requests.get(tasks_url).json()
    user_info = requests.get(user_url).json()
    e_username = user_info.get("username")
    users_l = []
    users_d = {}
    for task in tasks:
        dict = {}
        dict['task'] = task.get('title')
        dict['completed'] = task.get('completed')
        dict['username'] = e_username
        users_l.append(dict)
    users_d[USER_ID] = users_l
    with open(f"{USER_ID}.json", 'w') as file:
        json.dump(users_d, file)


if __name__ == "__main__":
    main()
