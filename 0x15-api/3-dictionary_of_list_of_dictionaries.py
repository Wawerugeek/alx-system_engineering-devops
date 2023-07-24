#!/usr/bin/python3
""""
this scrit reads data from an API"""
import json
import requests


def main():
    """This script reads data from public API and
    information about ALL users in json format"""
    users_url = "https://jsonplaceholder.typicode.com/users"
    users = requests.get(users_url).json()
    users_d = {}
    for user in users:
        EMPLOYEE_NAME = user.get("username")
        USER_ID = user.get("id")
        tasks_url = ("https://jsonplaceholder.typicode.com/users/{}/todos".
                     format(USER_ID))
        tasks = requests.get(tasks_url).json()
        user_l = []
        for task in tasks:
            dict = {}
            dict['username'] = EMPLOYEE_NAME
            dict['task'] = task.get('title')
            dict['completed'] = task.get('completed')
            user_l.append(dict)
        users_d[USER_ID] = user_l
    with open("todo_all_employees.json", "w") as file:
        json.dump(users_d, file)


if __name__ == "__main__":
    main()
