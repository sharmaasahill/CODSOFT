class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        if self.contacts:
            print("\nCONTACT LIST:")
            print("--------------")
            for index, contact in enumerate(self.contacts, start=1):
                print(f"{index}. Name: {contact.name}")
                print(f"   Phone: {contact.phone_number}")
                print(f"   Email: {contact.email}")
                print(f"   Address: {contact.address}")
                print()
        else:
            print("Contact list is empty.")

    def search_contact(self, search_term):
        found_contacts = []
        for contact in self.contacts:
            if (search_term.lower() in contact.name.lower()) or (search_term in contact.phone_number):
                found_contacts.append(contact)
        return found_contacts

    def update_contact(self, contact_index, updated_contact):
        self.contacts[contact_index] = updated_contact

    def delete_contact(self, contact_index):
        del self.contacts[contact_index]

def main():
    contact_book = ContactBook()

    while True:
        print("\nCONTACT BOOK MENU:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            print("\nADD CONTACT:")
            name = input("Enter contact name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email address: ")
            address = input("Enter address: ")
            contact = Contact(name, phone_number, email, address)
            contact_book.add_contact(contact)
            print("Contact added successfully.")

        elif choice == "2":
            contact_book.view_contacts()

        elif choice == "3":
            print("\nSEARCH CONTACT:")
            search_term = input("Enter name or phone number to search: ")
            found_contacts = contact_book.search_contact(search_term)
            if found_contacts:
                print("\nFOUND CONTACTS:")
                print("---------------")
                for contact in found_contacts:
                    print(f"Name: {contact.name}")
                    print(f"Phone: {contact.phone_number}")
                    print(f"Email: {contact.email}")
                    print(f"Address: {contact.address}\n")
            else:
                print("No matching contacts found.")

        elif choice == "4":
            print("\nUPDATE CONTACT:")
            contact_book.view_contacts()
            if contact_book.contacts:
                try:
                    index = int(input("Enter the index of contact to update: ")) - 1
                    if 0 <= index < len(contact_book.contacts):
                        name = input("Enter updated name: ")
                        phone_number = input("Enter updated phone number: ")
                        email = input("Enter updated email address: ")
                        address = input("Enter updated address: ")
                        updated_contact = Contact(name, phone_number, email, address)
                        contact_book.update_contact(index, updated_contact)
                        print("Contact updated successfully.")
                    else:
                        print("Invalid contact index.")
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")

        elif choice == "5":
            print("\nDELETE CONTACT:")
            contact_book.view_contacts()
            if contact_book.contacts:
                try:
                    index = int(input("Enter the index of contact to delete: ")) - 1
                    if 0 <= index < len(contact_book.contacts):
                        contact_book.delete_contact(index)
                        print("Contact deleted successfully.")
                    else:
                        print("Invalid contact index.")
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")

        elif choice == "6":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
