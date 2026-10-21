contacts = {}
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    contacts[name] = phone
    print("Contact saved")
while True:
    print("\n1. Add contact")
    print("2. View contacts")
    print("3. Search contact")
    print("4. Exit")
    choice = input("Choose: ")
    if choice == "1":
        add_contact()
    elif choice == "2":
        for name, phone in contacts.items():
            print(name, ":", phone)
    elif choice == "3":
        name = input("Enter name to search: ")
        print(contacts.get(name, "Contact not found"))
    elif choice == "4":
        break
