items = []
while True:
    print("\n1. Add")
    print("2. View")
    print("3. Sort")
    print("4. Remove")
    print("5. Exit")
    choice = input("Choose: ")
    if choice == "1":
        item = input("Enter item: ")
        items.append(item)
    elif choice == "2":
        for item in items:
            if item == "":
                continue
            print(item)
    elif choice == "3":
        items.sort()
        print(items)
    elif choice == "4":
        item = input("Enter item to remove: ")
        if item in items:
            items.remove(item)
        else:
            print("Item not found")
    elif choice == "5":
        print("Exit")
        break
    else:
        print("Invalid choice")
