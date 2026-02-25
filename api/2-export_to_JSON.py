#!/usr/bin/python3
"""Script to export employee TODO list to JSON"""
import json
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    user = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    tasks = [{"task": task.get("title"), "completed": task.get("completed"),
              "username": user.get("username")} for task in todos]

    with open(f"{employee_id}.json", "w") as jsonfile:
        json.dump({employee_id: tasks}, jsonfile)
