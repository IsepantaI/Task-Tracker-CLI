import json
import shlex
import atexit

def read_file():
    with open("tasks.json", "r") as f:
        data = json.load(f)
    return data

def save_to_file(data):
    with open("tasks.json", "w") as f:
        json.dump(data, f, indent=4)


data = read_file()
atexit.register(lambda: save_to_file(data))
while(True):
    input_str = input()

    input_split = shlex.split(input_str)

    if(input_split[0]!='task-cli'):
        print(f'{input_split[0]} is not a command!')
        exit()

    command = input_split[1]


    if(command == 'add'):
        description = input_split[2]
        data["last_id"] = data["last_id"] + 1;
        new_task = {
            'id': data["last_id"],
            'description': description,
            'status': 'todo' 
        }
        data["tasks"].append(new_task)
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)

    print(data["tasks"])

