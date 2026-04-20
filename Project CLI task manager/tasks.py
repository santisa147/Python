
def add_tasks(tasks):
    task = {'title': input("Task Name: "), 'done' : False}
    if task not in tasks:
            tasks.append(task)
    else: print('The Task is already added')

def view_tasks(tasks):
    for i, task in enumerate(tasks, start=1):
        status = "✅" if task["done"] else "❌"
        print(f"{i}. {task['title']} {status}")

def mark_done(tasks):
    a = 0
    view_tasks(tasks)
    a = int(input('Select the Task to Mark Done: ')) - 1
    tasks[a]['done']= True if tasks[a]['done'] == False  else print('The task is already Done')
    
def delete_task(tasks):
    a = 0
    view_tasks(tasks)
    a = int(input('Select the Task to Delete: ')) - 1
    tasks.pop(a)
    
def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            line = f"{task['title']}|{task['done']}\n"
            file.write(line)

def load_tasks():
    tasks = []
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                title, done = line.strip().split("|")
                tasks.append({
                    "title": title,
                    "done": done == "True"
                })
    except FileNotFoundError:
        pass
    return tasks

tasks = load_tasks()
while True:
   
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Exit")

    choice = str(input("Choose an option: "))
    if choice == "1":
        add_tasks(tasks)
    elif choice == '2':
       view_tasks(tasks)
    elif choice == '3':
        mark_done(tasks)
    elif choice == '4':
        delete_task(tasks)
    elif choice == '5':
        save_tasks(tasks)
        break
    else:print('Select a correct option')


        