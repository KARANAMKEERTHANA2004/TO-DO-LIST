# To-Do List Program: Shows specific message if no tasks entered

tasks = []

def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. View Tasks")
    print("2. Add Tasks")
    print("3. Remove Task")
    print("4. Quit")

def view_tasks():
    if tasks:  # If there are tasks, show them
        print("\nYour Tasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
    else:
        # Show this specific message if no tasks have been added
        print("\nNo tasks entered. Please enter the tasks.")
    input("Press Enter to return to menu...")

def add_tasks():
    print("Enter tasks. Type 'done' to finish.")
    count_before = len(tasks)
    while True:
        task = input("Enter task: ")
        if task.strip().lower() == "done":
            break
        elif task.strip():
            tasks.append(task.strip())
            print("Task added!")
        else:
            print("Please enter a valid task.")
    if len(tasks) > count_before:
        print("\nAll tasks now:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
    input("Press Enter to return to menu...")

def remove_task():
    if tasks:
        print("\nYour Tasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
        try:
            num = int(input("Enter task number to remove: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                print(f"Removed: {removed}")
                if tasks:
                    print("\nTasks left:")
                    for idx, task in enumerate(tasks, 1):
                        print(f"{idx}. {task}")
            else:
                print("Invalid number.")
        except ValueError:
            print("Please enter a valid number.")
        input("Press Enter to return to menu...")
    else:
        # No message needed if no tasks to remove
        pass

while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_tasks()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        print("Thank you!See you soon.")
        break
    else:
        print("Invalid choice. Please select 1-4.")