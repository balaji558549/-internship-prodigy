import json

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class ContactManager:
    def __init__(self, filename='contacts.json'):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_contacts(self):
        with open(self.filename, 'w') as file:
            json.dump(self.contacts, file)

    def add_contact(self, name, phone, email):
        new_contact = Contact(name, phone, email)
        self.contacts.append(new_contact.__dict__)
        self.save_contacts()

    def view_contacts(self):
        for contact in self.contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

    def edit_contact(self, name, new_phone=None, new_email=None):
        for contact in self.contacts:
            if contact['name'] == name:
                if new_phone:
                    contact['phone'] = new_phone
                if new_email:
                    contact['email'] = new_email
                self.save_contacts()
                return
        print("Contact not found.")

    def delete_contact(self, name):
        self.contacts = [contact for contact in self.contacts if contact['name'] != name]
        self.save_contacts()

def main():
    manager = ContactManager()
    while True:
        print("\n1. Add Contact\n2. View Contacts\n3. Edit Contact\n4. Delete Contact\n5. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            manager.add_contact(name, phone, email)
        elif choice == '2':
            manager.view_contacts()
        elif choice == '3':
            name = input("Enter the name of the contact to edit: ")
            new_phone = input("Enter new phone (leave blank to keep current): ")
            new_email = input("Enter new email (leave blank to keep current): ")
            manager.edit_contact(name, new_phone if new_phone else None, new_email if new_email else None)
        elif choice == '4':
            name = input("Enter the name of the contact to delete: ")
            manager.delete_contact(name)
        elif choice == '5':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
