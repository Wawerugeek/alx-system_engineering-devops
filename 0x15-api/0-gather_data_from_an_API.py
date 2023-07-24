#!/usr/bin/python3
"""This script gathers data from an API"""
import requests
import sys


def main():
    """Read information from a public API
    and return employees and their tasks completed"""
    emp_id = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(emp_id)
    tasks_url = (
        "https://jsonplaceholder.typicode.com/users/{}/todos".format(emp_id)
    )
    res = requests.get(tasks_url)
    tasks = res.json()
    user = requests.get(user_url).json()
    EMPLOYEE_NAME = user["name"]
    completed_tasks = [x for x in tasks if x['completed']]
    NUMBER_OF_DONE_TASKS = len(completed_tasks)
    TOTAL_NUMBER_OF_TASKS = len(tasks)

    print(
        f"Employee {EMPLOYEE_NAME} is done \
        with tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):"
    )

    for task in completed_tasks:
        print("\t {}".format(task["title"]))


if __name__ == "__main__":
    main()
