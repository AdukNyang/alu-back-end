#!/usr/bin/python3
"""Script to export employee TODO list to CSV"""
import csv
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    
    user = requests.get(user_url).json()
    todos = requests.get(todos_url).json()
    
    with open(f"{employee_id}.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([employee_id, user.get("username"),
                           task.get("completed"), task.get("title")])
