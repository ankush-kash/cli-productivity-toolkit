import json
from pathlib import Path

TODO_FILE = Path("data/todos.json")


def load_tasks():

    if not TODO_FILE.exists():
        return []
    
    with open(TODO_FILE,'r') as f:
        return json.load(f)

def save_tasks(tasks):

    with open(TODO_FILE,'w') as f:
        json.dump(tasks,f,indent=4)

def add_task(task):
    tasks = load_tasks()
    
    tasks.append({
        'task' : task,
        'done' : False
    })

    save_tasks(tasks)

    print('Task Added !!')

def list_tasks():

    tasks = load_tasks()

    if not tasks :
        print("No tasks Found !!")
    
    for index,task in enumerate(tasks):

        status = "✓" if task["done"] else "✗"

        print(f'{index}. [{status}] {task}')
        

def mark_done(task_number):

    tasks = load_tasks()

    index = task_number - 1

    if 0 <= index < len(tasks):

        tasks[index]['done'] = True

        save_tasks(tasks)

        print("Task marked as completed !!")

    else:
        print("Invalid task Number.")

def delete_task(task_number):

    tasks = load_tasks()
    
    index = task_number - 1

    if 0 <= index < len(tasks):
        removed = tasks.pop(index)

        save_tasks(tasks)

        print(f'Deleted : {removed['task']}')
    
    else:
        print("Invalid task number.")

