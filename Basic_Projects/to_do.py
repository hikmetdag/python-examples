tasks = []


def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added successfully.")


def delete_task(index):
    if 0 <= index <= len(tasks):
        deleted_task = tasks.pop(index - 1)
        print(f"Task '{deleted_task}' at index {index} deleted successfully.")
    else:
        print(f"Invalid task number. Please enter a valid index.")


def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")


def main():
    while True:
        print("\nTodo List Menu:")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. View Tasks")
        print("4. Exit")

        choice = input("Enter choice (1/2/3/4): ")

        if choice == "4":
            print("Exiting Todo List. Goodbye!")
            break
        if choice == "1":
            task = input("Enter task: ")
            add_task(task)

        elif choice == "2":
            task = int(input("Enter number of task to delete: "))
            delete_task(task)

        elif choice == "3":
            view_tasks()

        else:
            print("Invalid input. Please enter a valid choice (1/2/3/4).")


main()
