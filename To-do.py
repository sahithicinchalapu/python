
# list = [t1,t2,t3.....]
# print "To do list app!"
# operations:
# 1. add a task 
#      enter a task:
# 2. print all tasks
#     for loop print one by one with tick mark at the end for completed tasks
# 3. update any task
#     enter the task to be updated:
#     enter the new task:
# 4. delete task
#     enter the task to be deleted:
# 
tasks = []
print("\n**To-Do List**")
while True:
    
    print("1. Add a task")
    print("2. Show all tasks")
    print("3. Update a task")
    print("4. Delete a task")
    print("5. Exit")

    op = int(input("Enter your choice (1-5): "))

    if op == 1:
        task = input("Enter the task: ")
        tasks.append(task)
        print("Task added!")

    elif op == 2:
        if not tasks:
            print("No tasks available.")
        else:
            print("Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif op == 3:
        old_task = input("Enter the task to be updated: ")
        if old_task in tasks:
            new_task = input("Enter the new task: ")
            index = tasks.index(old_task)
            tasks[index] = new_task
            print("Task updated!")
        else:
            print(f"No task named '{old_task}'")

    elif op == 4:
        del_task = input("Enter the task to be deleted: ")
        if del_task in tasks:
            tasks.remove(del_task)
            print("Task deleted!")
        else:
            print(f"No task named '{del_task}'")

    elif op == 5:
        print("Exiting To-Do List. Bye!")
        break

    else:
        print("Invalid choice! Please enter 1-5.")
