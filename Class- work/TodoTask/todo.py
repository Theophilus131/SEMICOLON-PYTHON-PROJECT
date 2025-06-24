
tasks = []

def add_task(task):
    tasks.append(task)
    return "tasks added successfully"

def view_tasks():
    if len(tasks) == 0:
        print("No tasks available.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

