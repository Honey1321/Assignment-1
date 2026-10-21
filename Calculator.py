def calculator():
    while True:
        print("\n1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        choice = input("Enter choice: ")
        if choice == "5":
            print("Exit")
            break
        if choice not in ("1", "2", "3", "4"):
            print("Invalid choice")
            continue
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        if choice == "1":
            print("Result:", a + b)
        elif choice == "2":
            print("Result:", a - b)
        elif choice == "3":
            print("Result:", a * b)
        elif choice == "4":
            if b != 0:
                print("Result:", a / b)
            else:
                print("Cannot divide by zero")
calculator()
