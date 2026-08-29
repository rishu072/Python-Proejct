contacts = {}

while True:
    print("\nContact Book App")
    print("1. Add Contact")
    print("2. View Contacts") 
    print("3. Update Contact")  
    print("4. Search Contact")
    print("5. Delete Contact")
    print("6. Count Contacts")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == '1':
        name = input("Enter contact name: ")
        if name in contacts:
            print(f"Contact '{name}' already exists.")
        else:
            age = input("Enter contact age: ")
            email = input("Enter contact email: ")
            phone = input("Enter contact phone number: ")
            contacts[name] = {'age': age, 'email': email, 'phone': phone}
            print(f"Contact '{name}' added successfully.")

    elif choice == '2':
        name = input("Enter contact name to view: ")
        if name in contacts:
            contact = contacts[name]
            print(f"Name: {name}")
            print(f"Age: {contact['age']}")
            print(f"Email: {contact['email']}")
            print(f"Phone: {contact['phone']}")
        else:
            print(f"Contact '{name}' not found.")

    elif choice == '3':
        name = input("Enter contact name to update: ")
        if name in contacts:
            age = input("Enter new contact age: ")
            email = input("Enter new contact email: ")
            phone = input("Enter new contact phone number: ")
            contacts[name] = {'age': age, 'email': email, 'phone': phone}
            print(f"Contact '{name}' updated successfully.")
        else:
            print(f"Contact '{name}' not found.")

    elif choice == '4':
        name = input("Enter contact name to search: ")
        if name in contacts:
            contact = contacts[name]
            print(f"Name: {name}")
            print(f"Age: {contact['age']}")
            print(f"Email: {contact['email']}")
            print(f"Phone: {contact['phone']}")
        else:
            print(f"Contact '{name}' not found.")

    elif choice == '5':
        name = input("Enter contact name to delete: ")
        if name in contacts:
            del contacts[name]
            print(f"Contact '{name}' deleted successfully.")
        else:
            print(f"Contact '{name}' not found.")

    elif choice == '6':
        print(f"Total contacts: {len(contacts)}")

    elif choice == '7':
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")