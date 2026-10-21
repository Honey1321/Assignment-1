tasks = []
notes = {}
favourite_words = set()

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task saved")

def add_note():
    title = input("Note title: ")
    content = input("Note content: ")
    notes[title] = content
    print("Note saved")

while True:
    print("\n===== PERSONAL ASSISTANT =====")
    print("1. Add task")
    print("2. View tasks")
    print("3. Add note")
    print("4. View notes")
    print("5. Save favourite word")
    print("6. View favourite words")
    print("7. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        if not tasks:
            print("No tasks")
            continue

        for i, task in enumerate(tasks, start=1):
            print(i, task)

    elif choice == "3":
        add_note()

    elif choice == "4":
        for title, content in notes.items():
            print(title, ":", content)

    elif choice == "5":
        word = input("Enter favourite word: ").lower()
        favourite_words.add(word)
        print("Word saved")

    elif choice == "6":
        print(favourite_words)

    elif choice == "7":
        print("Exit")
        break

    else:
        print("Invalid choice")
