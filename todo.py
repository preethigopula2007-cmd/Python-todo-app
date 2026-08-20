def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            return [line.strip() for line in f]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")

def show_menu():
    print("\n--- TO-DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

tasks = load_tasks()

while True:
    show_menu()
    choice = input("Enter choice (1-5): ")

    if choice == "1":
        task = input("Enter new task: ")
        tasks.append(task)
        save_tasks(tasks)
        print(f"Added: {task}")

    elif choice == "2":
        if not tasks:
            print("No tasks yet!")
        else:
            print("\nYour Tasks:")
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")

    elif choice == "3":
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t}")
        num = int(input("Enter task number to mark done: ")) - 1
        if 0 <= num < len(tasks):
            tasks[num] = tasks[num] + " (Done)"
            save_tasks(tasks)
            print("Marked as done!")

    elif choice == "4":
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t}")
        num = int(input("Enter task number to delete: ")) - 1
        if 0 <= num < len(tasks):
            removed = tasks.pop(num)
            save_tasks(tasks)
            print(f"Deleted: {removed}")

    elif choice == "5":
        print("Bye! Tasks saved")
        break

    else:
        print("Invalid choice, try again!")
