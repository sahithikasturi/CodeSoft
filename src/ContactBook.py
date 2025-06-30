contacts = []

def display_menu():
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def add_contact():
    print("\nAdd New Contact")
    store_name = input("Store Name: ").strip()
    phone = input("Phone Number: ").strip()
    email = input("Email: ").strip()
    address = input("Address: ").strip()
    
    if not store_name or not phone:
        print("Error: Store Name and Phone Number are required!")
        return
    
    contacts.append({
        'store_name': store_name,
        'phone': phone,
        'email': email,
        'address': address
    })
    print(f"✅ Contact for {store_name} added successfully!")

def view_contacts():
    print("\nContact List")
    if not contacts:
        print("No contacts available")
        return
    
    print(f"{'No.':<4} {'Store Name':<20} {'Phone':<15}")
    for i, contact in enumerate(contacts, 1):
        print(f"{i:<4} {contact['store_name']:<20} {contact['phone']:<15}")

def search_contact():
    term = input("\nEnter search term (name or phone): ").strip().lower()
    if not term:
        print("Please enter a search term")
        return
    
    results = [
        c for c in contacts
        if term in c['store_name'].lower() or term in c['phone']
    ]
    
    if not results:
        print("No matching contacts found")
        return
    
    print(f"\nFound {len(results)} matching contact(s):")
    for i, contact in enumerate(results, 1):
        print(f"{i}. {contact['store_name']} - {contact['phone']}")

def update_contact():
    view_contacts()
    if not contacts:
        return
    
    try:
        contact_num = int(input("\nEnter contact number to update: "))
        if contact_num < 1 or contact_num > len(contacts):
            print("Invalid contact number")
            return
    except ValueError:
        print("Please enter a valid number")
        return
    
    contact = contacts[contact_num - 1]
    print(f"\nUpdating contact for {contact['store_name']}:")
    
    store_name = input(f"Store Name ({contact['store_name']}): ").strip()
    phone = input(f"Phone ({contact['phone']}): ").strip()
    email = input(f"Email ({contact['email']}): ").strip()
    address = input(f"Address ({contact['address']}): ").strip()
    
    if store_name:
        contact['store_name'] = store_name
    if phone:
        contact['phone'] = phone
    if email:
        contact['email'] = email
    if address:
        contact['address'] = address
    
    print("✅ Contact updated successfully!")

def delete_contact():
    view_contacts()
    if not contacts:
        return
    
    try:
        contact_num = int(input("\nEnter contact number to delete: "))
        if contact_num < 1 or contact_num > len(contacts):
            print("Invalid contact number")
            return
    except ValueError:
        print("Please enter a valid number")
        return
    
    deleted = contacts.pop(contact_num - 1)
    print(f"✅ Contact for {deleted['store_name']} deleted successfully!")

# Main program loop
while True:
    display_menu()
    try:
        choice = int(input("\nEnter your choice (1-6): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
    
    if choice == 1:
        add_contact()
    elif choice == 2:
        view_contacts()
    elif choice == 3:
        search_contact()
    elif choice == 4:
        update_contact()
    elif choice == 5:
        delete_contact()
    elif choice == 6:
        print("Exiting the Contact Management System. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1-6.")

    input("\nPress Enter to continue...")  # Pause before showing menu again