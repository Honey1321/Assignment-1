tasks = []
def show_tasks():
    if not tasks:
        print("No tasks available")
    else:
        for i, task in enumerate(tasks, start=1):
            print(i, task)
while True:
    print("\n1. Add task")
    print("2. View tasks")
    print("3. Complete/remove task")
    print("4. Exit")
    choice = input("Choose: ")
    if choice == "1":
        tasks.append(input("Enter task: "))
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        show_tasks()
        if tasks:
            number = int(input("Task number: "))
            if 1 <= number <= len(tasks):
                print("Completed:", tasks.pop(number - 1))
            else:
                print("Invalid number")
    elif choice == "4":
        break
