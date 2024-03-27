import os

# Function to display the menu options
def display_menu():
    print("COMMAND MENU")
    print("1. View all tasks")
    print("2. Add a task")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Exit")


# Function to view all tasks
def view_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            if tasks:
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task.strip()}")
            else:
                print("No tasks found.")
    else:
        print("No tasks found.")


# Function to add a task
def add_task():
    task = input("Enter the task: ")
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
    print("Task added successfully.")


# Function to mark a task as complete
def mark_complete():
    view_tasks()
    task_number = int(input("Enter the task number to mark as complete: "))
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1] = "[Completed] " + tasks[task_number - 1]
        with open("tasks.txt", "w") as file:
            file.writelines(tasks)
        print("Task marked as complete.")
    else:
        print("Invalid task number.")


# Function to delete a task
def delete_task():
    view_tasks()
    task_number = int(input("Enter the task number to delete: "))
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
    if 1 <= task_number <= len(tasks):
        del tasks[task_number - 1]
        with open("tasks.txt", "w") as file:
            file.writelines(tasks)
        print("Task deleted successfully.")
    else:
        print("Invalid task number.")


# Main function
def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            mark_complete()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
