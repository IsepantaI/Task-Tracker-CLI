import json
import shlex
import atexit
from datetime import datetime

def read_file():
    with open("data.json", "r") as f:
        data = json.load(f)
    return data

def save_to_file(data):
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)

def find_task_by_id(task_id):
    task_id = int(input_split[2])   
    task = next((task for task in data["tasks"] if task["id"] == task_id), None)
    return(task)

data = read_file()
atexit.register(lambda: save_to_file(data))
while(True):
    input_str = input()

    input_split = shlex.split(input_str)

    if(input_split[0]!='task-cli'):
        print(f'{input_split[0]} is not a command!')

    command = input_split[1]


    if(command == 'add'):
        description = input_split[2]
        data["last_id"] = data["last_id"] + 1;
        new_task = {
            'id': data["last_id"],
            'description': description,
            'status': 'todo',
            'createdAt': datetime.now().isoformat(),
            'updatedAT': datetime.now().isoformat()
        }
        data["tasks"].append(new_task)
        print(f'Task added successfully (ID: {new_task["id"]})')
    
    if(command == 'update'):
        task_id = int(input_split[2])   
        task_description = input_split[3]
        task = find_task_by_id(task_id)
        if task: 
            task["description"] = task_description
        else:
            print(f'no task exist with id {task_id}')

    if(command == 'delete'):
        task_id = int(input_split[2])   
        task = find_task_by_id(task_id)
        if task:
            data["tasks"].remove(task)
        else:
            print(f'no task exist with id {task_id}')
    
    if(command == 'mark-in-progress'):
        task_id = int(input_split[2])   
        task = find_task_by_id(task_id)
        if task:
            task["status"] = 'in-progress'
        else:
            print(f'no task exist with id {task_id}')

    if(command == 'mark-done'):
        task_id = int(input_split[2])   
        task = find_task_by_id(task_id)
        if task:
            task["status"] = 'done'
        else:
            print(f'no task exist with id {task_id}')

    if(command == 'list'):
        print('-------------')
        if(len(input_split) == 2):
            for task in data["tasks"]:
                print(task["description"],':', task["status"])
        else:
            for task in data["tasks"]:
                if(task["status"] == input_split[2]):
                    print(task["description"],':', task["status"])
        print('-------------')
            

