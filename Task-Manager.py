def load_tasks():
    try:
        with open("tasks.txt","r",encoding="UTF-8")as fbe:
            for line in fbe:
                tasks.append(line.strip().split("%%"))
    except FileNotFoundError:
        pass

def save_tasks():
    with open("tasks.txt","w",encoding="utf-8")as fki:
            for i in tasks:
                print(i[0],i[1],sep="%%",file=fki)
    

def show_tasks():
    if not(tasks):
            print("There's no tasks in your list.")
    else:
        show = input("Show all / completed / active tasks?: ")
        if show not in ["all","completed","active"]:
            print("Unknown command.")
            return
        else:
            c = 0
            if show == "all":
                for i in range(len(tasks)):
                    print(f"{i + 1}. {tasks[i][0]} {tasks[i][1]}")
            elif show == "completed":
                for i in range(len(tasks)):
                    if tasks[i][1] == "[✔]":
                        c += 1
                        print(f"{i + 1}. {tasks[i][0]} {tasks[i][1]}")
                if c == 0:
                    print("There's no completed task in your list.")
            elif show == "active":
                for i in range(len(tasks)):
                    if tasks[i][1] == "[ ]":
                        c += 1
                        print(f"{i + 1}. {tasks[i][0]} {tasks[i][1]}")
                if c == 0:
                    print("There's no active task in your list.")

def add_task():
    add = input("Enter task: ")
    tasks.append([add,"[ ]"])
    save_tasks()
    print("Task added.")

def edit_task():
    if not(tasks):
        print("Error. The list is empty.")
    else:
        edit = input("Enter task number: ")
        if not edit.isdigit():
            print("Please enter a valid number.")
            return
        else:
            edit = int(edit) - 1

        if 0 <= edit < len(tasks):
            add = input("Enter new task: ")
            tasks[edit][0] = add
            tasks[edit][1] = "[ ]"
            save_tasks()
            print("Task updated.")
        else:
            print("Invalid index number.")
            return

def complete_task():
    if not(tasks):
        print("Error. The list is empty.")
    else:
        index = input("Enter task number: ")
        if not index.isdigit():
            print("Please enter a valid number.")
            return
        else:
            index = int(index) - 1

        if 0 <= index < len(tasks):
            tasks[index][1] = "[✔]"
            save_tasks()
            print("Task completed.")
        else:
            print("Invalid index number.")
            return

def stats():
    total = len(tasks)
    completed = 0
    for i in tasks:
        if i[1] == "[✔]":
            completed += 1
    active = total - completed
    print(f"Total: {total}")
    print(f"Completed: {completed}")
    print(f"Active: {active}")

def remove_task():
    if not(tasks):
        print("Error. The list is empty.")
    else:
        remove = input("Enter task number: ")
        if remove.isdigit() and (0 <= int(remove)-1 < len(tasks)):
            remove = int(remove)
            delete = input("Confirm the delete (y/n): ")                    
            if delete == 'y':
                tasks.pop(remove - 1)
                save_tasks()
                print("Task deleted.")
            elif delete == 'n':
                print("Task not deleted.")  
        elif not(remove.isdigit()):
            print("Please enter a valid number.")
        elif not(0 <= int(remove)-1 < len(tasks)):
            print("Invalid index number.")

options = ["add", "show", "remove", "edit", "complete", "stats","quit"]
tasks = []
load_tasks()

while True:
    answer = input("add / show / remove / edit / complete / stats / quit\n")

    while answer not in options:
        print("Error. Unknown command. Please choose from the options below:")
        answer = input("add / show / remove / edit / complete / stats / quit\n")

    if answer == "quit":
        break
    
    elif answer == "show":
        show_tasks()
    
    elif answer == "add":
        add_task()
        
    elif answer == "edit":
        edit_task()
    elif answer == "complete":
        complete_task()
    elif answer == "stats":
        stats()
    else:
        remove_task()
