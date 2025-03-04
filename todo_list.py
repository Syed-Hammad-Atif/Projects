tasks = []

def menu():
    print("\n=== To-Do List ===")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Mark Complete")
    print("5. Exit")

def show_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("\nTasks:")
        for i, (name, done) in enumerate(tasks, start=1):
            status = "[✓]" if done else "[ ]"
            print(f"{i}. {status} {name}")

def get_valid_index():
    try:
        index = int(input("Enter task number: ")) - 1
        if 0 <= index < len(tasks):
            return index
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a number.")
    return None

def add_task():
    task_name = input("Enter task: ")
    tasks.append((task_name, False))
    print("Task added!")

def remove_task():
    show_tasks()
    index = get_valid_index()
    if index is not None:
        removed_task = tasks.pop(index)
        print(f"Removed: {removed_task[0]}")

def mark_complete():
    show_tasks()
    task_num = int(input("Enter task number to mark as complete: ")) - 1
    
    if 0 <= task_num < len(tasks):
        tasks[task_num] = (tasks[task_num][0], True)
        print(f"Task '{tasks[task_num][0]}' marked as complete!")
    else:
        print("Invalid task number. Please try again.")

def main():
    while True:
        menu()
        choice = input("Choose an option (1-5): ")
        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            mark_complete()
        elif choice == "5":
            print("Exiting!")
            break
        else:
            print("Invalid choice. Enter a number 1-5.")

if __name__ == "__main__":
    main()
