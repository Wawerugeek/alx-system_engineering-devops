#!/usr/bin/python3
"""READS DATA FROM API AND stores the data"""
import csv
import requests
import sys


def main():
    """This script reads data from a Fake API and
    stores the infomation in a csv file
    """
    USER_ID = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(USER_ID)
    tasks_url = ("https://jsonplaceholder.typicode.com/users/{}/todos".
                 format(USER_ID))
    tasks = requests.get(tasks_url).json()
    user_info = requests.get(user_url).json()
    employee_name = user_info.get("username")
    with open(f"{USER_ID}.csv", 'w') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([task.get('userId'), employee_name,
                             task.get('completed'), task.get('title')])


if __name__ == "__main__":
    main()
