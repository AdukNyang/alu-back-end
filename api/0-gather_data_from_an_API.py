#!/usr/bin/python3
"""Script to fetch and display employee TODO list progress from API"""
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    user = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    completed = [task for task in todos if task.get("completed")]

    print(f"Employee {user.get('name')} is done with tasks"
          f"({len(completed)}/{len(todos)}):")
    for task in completed:
        print(f"\t {task.get('title')}")
