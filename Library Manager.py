books = {
    "Python Basics": "available",
    "English Grammar": "available",
    "Computer Networks": "available"
}
borrowed = set()
while True:
    print("\n1. View books")
    print("2. Borrow book")
    print("3. Return book")
    print("4. Exit")
    choice = input("Choose: ")
    if choice == "1":
        for book, status in books.items():
            print(book, "-", status)
    elif choice == "2":
        book = input("Enter book name: ")
        if book in books and books[book] == "available":
            books[book] = "borrowed"
            borrowed.add(book)
            print("Book borrowed")
        else:
            print("Book unavailable or not found")
    elif choice == "3":
        book = input("Enter book name: ")
        if book in borrowed:
            books[book] = "available"
            borrowed.remove(book)
            print("Book returned")
        else:
            print("This book is not in the borrowed set")
    elif choice == "4":
        break
