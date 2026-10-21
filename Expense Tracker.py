expenses = []
def add_expense():
    name = input("Expense name: ")
    amount = float(input("Amount: "))
    expenses.append((name, amount))
while True:
    print("\n1. Add expense")
    print("2. View expenses")
    print("3. Total expenses")
    print("4. Exit")
    choice = input("Choose: ")
    if choice == "1":
        add_expense()
    elif choice == "2":
        for name, amount in expenses:
            print(name, "-", amount)
    elif choice == "3":
        total = 0
        for name, amount in expenses:
            total += amount
        print("Total expenses:", total)
    elif choice == "4":
        break
