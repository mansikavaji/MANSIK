gimport json

def load_contacts(filename="contacts.json"):
    try:
        with open(filename, "r") as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = []
    return contacts

def save_contacts(contacts, filename="contacts.json"):
    with open(filename, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    print("Contact added successfully!")

def view_contacts(contacts):
    print("\nContact List:")
    for contact in contacts:
        print(f"Name: {contact['name']}, Phone: {contact['phone']}")
    print()

def search_contact(contacts):
    search_term = input("Enter name or phone number to search: ")
    results = [contact for contact in contacts if search_term.lower() in contact['name'].lower() or search_term in contact['phone']]
    if results:
        print("\nSearch Results:")
        for contact in results:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
    else:
        print("No contacts found.")
    print()

def update_contact(contacts):
    search_term = input("Enter name or phone number of the contact to update: ")
    for contact in contacts:
        if search_term.lower() in contact['name'].lower() or search_term in contact['phone']:
            print(f"Updating contact: {contact['name']}")
            contact['name'] = input(f"Enter new name ({contact['name']}): ") or contact['name']
            contact['phone'] = input(f"Enter new phone number ({contact['phone']}): ") or contact['phone']
            contact['email'] = input(f"Enter new email ({contact['email']}): ") or contact['email']
            contact['address'] = input(f"Enter new address ({contact['address']}): ") or contact['address']
            print("Contact updated successfully!")
            return
    print("Contact not found.")

def delete_contact(contacts):
    search_term = input("Enter name or phone number of the contact to delete: ")
    for contact in contacts:
        if search_term.lower() in contact['name'].lower() or search_term in contact['phone']:
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return
    print("Contact not found.")

def main():
    contacts = load_contacts()
    
    while True:
        print("\nContact Book Menu")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ")
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            save_contacts(contacts)
            print("Contacts saved. Exiting...")
            break
        else:
            print("Invalid choice. Please choose again.")

# Run the main function
if __name__ == "__main__":
    main()
