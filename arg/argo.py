import argparse
import json
import os

# json_file = "todo_list.json"

def show_instructions():
    print("\n.........................................................INSTRUCTIONS...................................................")
    print("-  To add a task=> python scriptname.py add <task>")
    print("- To list all tasks=> python script.py list")
    print("- To mark a task as complete: python script.py complete <task_number>")
    print("......................................................................................................................\n")
def load_tasks():
    global json_file
    json_file = input("Enter the path to your JSON file: ").strip()

    if os.path.exists(json_file):
        with open(json_file, "r", encoding="utf-8") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []

def save_tasks(tasks):
    with open(json_file, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)

def add_task(description):
    tasks = load_tasks()
    tasks.append({"task": description, "completed": False})
    save_tasks(tasks)
    print(f"Task added: {description}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for index, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{index}.  {task['task']}=> {status}")

def complete_task(task_number):
    tasks = load_tasks()
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        save_tasks(tasks)
        print(f"Task {task_number} marked as complete.")
    else:
        print("Invalid task number.")

def main():

    parser = argparse.ArgumentParser(description="Command-line To-Do List")
    parser.add_argument("command", choices=["add", "list", "complete"], help="Action to perform")
    parser.add_argument("param", nargs="?", help="Task description or task number")
    
    try:
        args = parser.parse_args()
    except:
        print("Invalid command. Use 'add', 'list', or 'complete'.")
        show_instructions()   
        return
    
    if args.command == "add":
        if args.param:
            add_task(args.param)
        else:
            print("Please provide a task name.")
    elif args.command == "list":
        list_tasks()
    elif args.command == "complete":
        if args.param and args.param.isdigit():
            complete_task(int(args.param))
        else:
            print("Please provide a valid task number.")
main()
