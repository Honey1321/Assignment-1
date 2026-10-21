students = input("Enter student names separated by spaces: ").split()
present = set()
while True:
    print("\n1. Mark present")
    print("2. View attendance")
    print("3. Exit")
    choice = input("Choose: ")
    if choice == "1":
        name = input("Student name: ")
        if name in students:
            present.add(name)
            print("Attendance marked")
        else:
            print("Student not found")
    elif choice == "2":
        for name in students:
            if name in present:
                print(name, "- Present")
            else:
                print(name, "- Absent")
    elif choice == "3":
        break
