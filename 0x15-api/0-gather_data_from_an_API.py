#!/usr/bin/python3
'''
using this REST API, for a given employee ID,
returns information about his/her TODO list progress
'''
import re
import requests
import sys

url = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            id = int(sys.argv[1])
            user = requests.get('{}/users/{}'.format(url, id)).json()
            todo = requests.get('{}/todos'.format(url)).json()
            name = user.get('name')
            tasks = list(filter(lambda x: x.get('userId') == id, todo))
            completed_tasks = list(filter(lambda x: x.get('completed'), tasks))
            print(
                'Employee {} is done with tasks({}/{}):'.format(
                    name,
                    len(completed_tasks),
                    len(tasks)
                )
            )
            if len(completed_tasks) > 0:
                for task in completed_tasks:
                    print('\t {}'.format(task.get('title')))
