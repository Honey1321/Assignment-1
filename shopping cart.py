products = [
    ("Laptop", 50000),
    ("Phone", 20000),
    ("Mouse", 800),
    ("Keyboard", 1500)
]
cart = []
while True:
    print("\n1. View products")
    print("2. Add to cart")
    print("3. View cart")
    print("4. Checkout")
    print("5. Exit")
    choice = input("Choose: ")
    if choice == "1":
        for i, product in enumerate(products, start=1):
            print(i, product[0], "-", product[1])
    elif choice == "2":
        number = int(input("Enter product number: "))
        if 1 <= number <= len(products):
            cart.append(products[number - 1])
            print("Added to cart")
        else:
            print("Invalid product")
    elif choice == "3":
        for name, price in cart:
            print(name, "-", price)
    elif choice == "4":
        total = 0
        for name, price in cart:
            total += price
        print("Total amount:", total)
        print("Checkout completed")
        break
    elif choice == "5":
        print("Exit")
        break
