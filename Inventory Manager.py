inventory = {
    "pen": 10,
    "book": 5,
    "pencil": 20
}
def view_inventory():
    for item, quantity in inventory.items():
        print(item, "-", quantity)
while True:
    print("\n1. View inventory")
    print("2. Add stock")
    print("3. Sell stock")
    print("4. Exit")
    choice = input("Choose: ")
    if choice == "1":
        view_inventory()
    elif choice == "2":
        item = input("Item name: ").lower()
        quantity = int(input("Quantity to add: "))
        inventory[item] = inventory.get(item, 0) + quantity
        print("Stock updated")
    elif choice == "3":
        item = input("Item name: ").lower()
        quantity = int(input("Quantity to sell: "))
        if item in inventory and inventory[item] >= quantity:
            inventory[item] -= quantity
            print("Sale completed")
        else:
            print("Insufficient stock or item not found")
    elif choice == "4":
        break
