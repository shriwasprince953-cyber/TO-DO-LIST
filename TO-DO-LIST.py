tasks = []
print("========== TO DO LIST ==========")

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")
    user = input("Choose your operation: ")
    if user == "1":
        task = input("Enter your task: ")
        tasks.append(task)
        print("Task added successfully!")
    elif user == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(i, ".", task)
    elif user == "3":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            print("\nTasks:")
            for i, task in enumerate(tasks, start=1):
                print(i, ".", task)
            delete = int(input("Enter task number to delete: "))
            if 1 <= delete <= len(tasks):
                removed = tasks.pop(delete - 1)
                print(removed, "deleted successfully!")
            else:
                print("Invalid task number.")
    elif user == "4":
        print("Exiting To-Do List...")
        break
    else:
        print("Invalid choice.")