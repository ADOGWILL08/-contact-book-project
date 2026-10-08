# Contact Book Console Application
# SBA 351 - Python Essentials 1
#
# Contacts are stored in a dictionary:
#   key   = the contact's name
#   value = the contact's phone number


def show_menu():
    """Print the menu of choices for the user."""
    print("\nContact Book Menu:")
    print("1. Add New Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")


def add_contact(contacts):
    """Ask for a name and phone number, then add them to the contacts dictionary.

    Returns True if the contact was added, or False if something was invalid
    (empty name, duplicate name, or bad phone number).
    """
    # .strip() removes extra spaces at the start and end of what the user typed
    name = input("Enter the contact's name: ").strip()

    # Validation 1: the name cannot be empty
    if name == "":
        print("Error: name cannot be empty.")
        return False

    # Validation 2: a name can only exist once in the dictionary
    if name in contacts:
        print(f"Error: '{name}' already exists. No duplicate was added.")
        return False

    phone = input("Enter the phone number (digits only, 7-15 digits): ").strip()

    # Validation 3: phone must be all digits and a reasonable length
    if not phone.isdigit() or not (7 <= len(phone) <= 15):
        print("Error: phone number must contain only digits and be 7 to 15 digits long.")
        return False

    # Everything is valid, so save the contact (name is the key, phone is the value)
    contacts[name] = phone
    print(f"Contact '{name}' added successfully.")
    return True


def view_contacts(contacts):
    """Display every contact in alphabetical order by name.

    If the dictionary is empty, print a message saying so instead.
    """
    # An empty dictionary counts as False, so "not contacts" means "no contacts"
    if not contacts:
        print("The contact list is empty.")
        return

    print("\n--- All Contacts ---")
    # sorted(..., key=str.lower) puts names in A-Z order, ignoring upper/lowercase
    # enumerate(..., start=1) gives each contact a number starting at 1
    for number, name in enumerate(sorted(contacts, key=str.lower), start=1):
        print(f"{number}. {name}: {contacts[name]}")


def search_contact(contacts):
    """Search for contacts whose name contains the text the user types.

    Partial matches are allowed and capital letters are ignored.
    Returns a list of the names that matched (empty if none).
    """
    term = input("Enter a name (or part of a name) to search for: ").strip()

    # Validation: the search text cannot be empty
    if term == "":
        print("Error: search text cannot be empty.")
        return []

    # Loop through every name and keep the ones that contain the search text.
    # .lower() on both sides makes the search ignore upper/lowercase.
    matches = []
    for name in contacts:
        if term.lower() in name.lower():
            matches.append(name)

    # If nothing matched, tell the user and stop here
    if not matches:
        print(f"No contacts found matching '{term}'.")
        return matches

    # Otherwise print each match with its phone number, in A-Z order
    print(f"\n--- Search Results for '{term}' ---")
    for name in sorted(matches, key=str.lower):
        print(f"{name}: {contacts[name]}")
    return matches


def delete_contact(contacts):
    """Ask for a name and remove that contact from the dictionary.

    Returns True if a contact was deleted, or False if the name was
    empty or was not found.
    """
    name = input("Enter the name of the contact to delete: ").strip()

    # Validation: the name cannot be empty
    if name == "":
        print("Error: name cannot be empty.")
        return False

    # If the name is a key in the dictionary, remove it and confirm
    if name in contacts:
        del contacts[name]  # del removes the key and its phone number together
        print(f"Contact '{name}' was deleted.")
        return True

    # Otherwise the name is not in the dictionary
    print(f"Error: no contact named '{name}' was found.")
    return False


def main():
    """Run the program: show the menu in a loop until the user exits."""
    contacts = {}  # empty dictionary that will hold all contacts

    while True:
        show_menu()

        # try/except stops the program from crashing if the user
        # types letters instead of a number
        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("Error: please enter a number from 1 to 5.")
            continue  # go back to the top of the loop and show the menu again

        if choice == 1:
            add_contact(contacts)
        elif choice == 2:
            view_contacts(contacts)
        elif choice == 3:
            search_contact(contacts)
        elif choice == 4:
            delete_contact(contacts)
        elif choice == 5:
            print("Goodbye!")
            break  # leave the loop, which ends the program
        else:
            print("Error: invalid choice. Please choose a number from 1 to 5.")


main()