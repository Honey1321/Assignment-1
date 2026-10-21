balance = 1000
def deposit(balance):
    amount = float(input("Enter deposit amount: "))
    if amount > 0:
        balance += amount
        print("Deposit successful")
    else:
        print("Enter a positive amount")
    return balance
def withdraw(balance):
    amount = float(input("Enter withdrawal amount: "))
    if amount <= 0:
        print("Enter a positive amount")
    elif amount <= balance:
        balance -= amount
        print("Withdrawal successful")
    else:
        print("Insufficient balance")
    return balance
while True:
    print("\n1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = input("Choose: ")
    if choice == "1":
        print("Balance:", balance)
    elif choice == "2":
        balance = deposit(balance)
    elif choice == "3":
        balance = withdraw(balance)
    elif choice == "4":
        print("Exit")
        break
