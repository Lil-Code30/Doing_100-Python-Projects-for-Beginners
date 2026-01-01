print("Input values:")
print("1. Add Task")
print("2. Edit Task")
print("3. Delete Task")
print("4. Exit")
print("")
tasks = []
isExit = False

def print_all_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return

    # Table header
    print("+-------+----------------------+")
    print("| Index | Task Name            |")
    print("+-------+----------------------+")

    # Rows
    for i, task in enumerate(tasks):
        print(f"| {i:<5} | {task:<20} |")

    # Footer
    print("+-------+----------------------+")
    print("")


while(isExit != True):
    option = int(input("Select an option: "))
    if(option not in [1, 2, 3, 4]):
        print("Wrong Option")
        isExit = True
    else:
        match(option):
            case 1:
                task = input("Enter a task: ")
                tasks.append(task)
                print("Task added successfully.")
                print_all_tasks(tasks)
                
            case 2: 
                if len(tasks) > 0:
                    taskIndex = int(input("Enter task index to edit:"))
                    if(taskIndex >= len(tasks)):
                        print("Wrong task index.")
                        isExit = True
                    else:
                        newTask = input("Enter new task: ")
                        tasks[taskIndex] = newTask
                        print("Task edited successfully.")
                        print_all_tasks(tasks)
                else:
                    print("No Tasks Available.")
            case 3: 
                taskIndex = int(input("Enter task index to delete: "))
                if(taskIndex >= len(tasks)):
                    print("Wrong task index.")
                    isExit = True
                else:
                    tasks.pop(taskIndex)
                    print("Task deleted successfully.")
                    print_all_tasks(tasks)
            case 4:
                isExit = True
                print("GoodBye :)")
            case _:
                print("Wrong option selected, Start Again")
                
