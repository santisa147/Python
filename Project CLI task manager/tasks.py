tasks = []

while True:
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Exit")

    choice = str(input("Choose an option: "))
    if choice == "1":
        task = {'title': input("Task Name: "), 'done' : False}
        if task not in tasks:
            tasks.append(task)
        else: print('The Task is already added')
    elif choice == '2':
        print(tasks)
    elif choice == '3':
        a=0
        for i in tasks:
            a=a+1
            print(a, i)
        a = int(input('Select the Task to mark done: ')) - 1
        if tasks[a]['done'] == False:
            tasks[a]['done']= True
        else: print('The task is already Done')
    elif choice == '4':
        a=0
        for t in tasks:
            a=a+1
            print(a, t)
        a = int(input('Select the Task to Delete: ')) - 1
        tasks.pop(a)
    elif choice == '5':
        break
    else:print('Select a correct option')