import os

FILE_NAME = "tasks.txt"

# Load tasks
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return f.read().splitlines()
    return []

# Save tasks
def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        for task in tasks:
            f.write(task + "\n")

# Show tasks
def show_tasks(tasks):
    if not tasks:
        print("No tasks found!")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

# Main program
tasks = load_tasks()

while True:
    print("\n1. View Tasks\n2. Add Task\n3. Delete Task\n4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        show_tasks(tasks)

    elif choice == "2":
        task = input("Enter new task: ")
        tasks.append(task)
        save_tasks(tasks)
        print("Task added!")

    elif choice == "3":
        show_tasks(tasks)
        num = int(input("Enter task number to delete: "))
        if 0 < num <= len(tasks):
            tasks.pop(num - 1)
            save_tasks(tasks)
            print("Task deleted!")
        else:
            print("Invalid number!")

    elif choice == "4":
        break

    else:
        print("Invalid choice!")