import os

tasks_file = "demo.txt"

# Load tasks from file
def load_tasks():
    if not os.path.exists(tasks_file):
        return []
    with open(tasks_file, "r") as file:
        tasks = [task.strip() for task in file.readlines()]
    return tasks

# Save tasks to file
def save_tasks(tasks):
    with open(tasks_file, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Add task
def add_task():
    task = input("Enter task: ")
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully.")

# View tasks
def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks added.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

# Update task
def update_task():
    tasks = load_tasks()
    view_tasks()

    try:
        index = int(input("Enter task number to update: ")) - 1
        if 0 <= index < len(tasks):
            new_task = input("Enter new task: ")
            tasks[index] = new_task
            save_tasks(tasks)
            print("Task updated successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Delete task
def delete_task():
    tasks = load_tasks()
    view_tasks()

    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed_task = tasks.pop(index)
            save_tasks(tasks)
            print("Deleted task:", removed_task)
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main menu
def main():
    while True:
        print("\nTo-Do List Menu")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

# Run program
if __name__ == "__main__":
    main()