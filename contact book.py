import os

FILE_NAME = "contacts.txt"

# Load contacts from file
def load_contacts():
    contacts = {}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                data = line.strip().split(",")
                if len(data) == 4:
                    name, phone, email, address = data
                    contacts[name] = {"phone": phone, "email": email, "address": address}
    return contacts

# Save contacts to file
def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        for name, details in contacts.items():
            file.write(f"{name},{details['phone']},{details['email']},{details['address']}\n")

# Display menu
def show_menu():
    print("\n --- Contact Management System ---")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

# Load existing contacts
contacts = load_contacts()

# Main loop
while True:
    show_menu()
    choice = input("\nEnter your choice (1-6): ").strip()

    if choice == "1":
        name = input("Enter name: ").strip()
        phone = input("Enter phone number: ").strip()
        email = input("Enter email: ").strip()
        address = input("Enter address: ").strip()

        if name in contacts:
            print(" Contact already exists! Use update option to modify.")
        else:
            contacts[name] = {"phone": phone, "email": email, "address": address}
            save_contacts(contacts)
            print(f" Contact '{name}' added successfully!")

    elif choice == "2":
        if contacts:
            print("\n --- Contact List ---")
            for name, details in sorted(contacts.items()):
                print(f"{name} | {details['phone']}")
        else:
            print("No contacts found.")

    elif choice == "3":
        query = input("Enter name or phone number to search: ").strip().lower()
        found = False
        for name, details in contacts.items():
            if query in name.lower() or query in details["phone"]:
                print(f"\n Name: {name}")
                print(f" Phone: {details['phone']}")
                print(f" Email: {details['email']}")
                print(f" Address: {details['address']}")
                found = True
        if not found:
            print("Contact not found.")

    elif choice == "4":
        name = input("Enter name to update: ").strip()
        if name in contacts:
            print("\nLeave field blank to keep old value.")
            phone = input(f"New phone ({contacts[name]['phone']}): ").strip()
            email = input(f"New email ({contacts[name]['email']}): ").strip()
            address = input(f"New address ({contacts[name]['address']}): ").strip()

            if phone:
                contacts[name]["phone"] = phone
            if email:
                contacts[name]["email"] = email
            if address:
                contacts[name]["address"] = address

            save_contacts(contacts)
            print(f" Contact '{name}' updated successfully!")
        else:
            print("Contact not found.")

    elif choice == "5":
        name = input("Enter name to delete: ").strip()
        if name in contacts:
            del contacts[name]
            save_contacts(contacts)
            print(f" Contact '{name}' deleted successfully!")
        else:
            print("Contact not found.")

    elif choice == "6":
        print("\n Exiting Contact Management System. Goodbye!")
        break

    else:
        print(" Invalid choice! Please enter a number between 1 and 6.")
