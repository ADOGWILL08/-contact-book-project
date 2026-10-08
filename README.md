# Contact Book Project

SBA 351 - Python Essentials 1

A console-based Contact Book application written in Python. The user chooses actions from a text menu to add, view, search, and delete contacts.

## Files in This Repository

- `contact_book.py` - the Contact Book program
- `interaction_log.txt` - console output from one complete test run
- `README.md` - this write-up

## How to Run

Open `contact_book.py` in VS Code and click the Run (play) button, or type `python contact_book.py` in a terminal opened in this folder.

## Features

1. **Add New Contact** - asks for a name and phone number. A name can only exist once; duplicates are rejected.
2. **View All Contacts** - lists every contact in alphabetical order, or says the list is empty.
3. **Search Contact** - finds contacts whose name contains the text typed (partial and case-insensitive), or says none were found.
4. **Delete Contact** - removes a contact by name and confirms, or says the name was not found.
5. **Exit** - ends the program.

The menu repeats after every action until the user chooses Exit.

## Program Structure

The program is organized into small functions, each with one job:

- `show_menu()` - prints the menu choices.
- `add_contact(contacts)` - gets a name and phone number, validates them, and stores the contact. Returns `True` if added or `False` if invalid.
- `view_contacts(contacts)` - prints all contacts sorted A-Z, or an "empty" message.
- `search_contact(contacts)` - loops through the names, collects the matches, and prints them. Returns the list of matching names.
- `delete_contact(contacts)` - removes a contact if it exists. Returns `True` if deleted or `False` if not.
- `main()` - creates the contacts dictionary and runs the menu loop.

## How Data Flows

1. `main()` creates one empty dictionary called `contacts`. The key is the contact's name and the value is the phone number.
2. A `while True` loop shows the menu and reads the user's choice.
3. The choice is converted to an integer inside a `try/except` block, so typing letters shows an error instead of crashing.
4. Based on the choice, `main()` calls one of the feature functions and passes the same `contacts` dictionary to it.
5. Each function reads or changes the dictionary directly, so changes made by one function (for example, adding a contact) are visible to the others (for example, viewing).
6. Choosing 5 prints a goodbye message and uses `break` to leave the loop and end the program.

## Input Validation

- Menu choice: letters cause a `ValueError` that is caught by `try/except`, and numbers outside 1-5 show an error. In both cases the menu is shown again.
- Name: cannot be empty, and cannot already exist in the dictionary (this keeps every name unique).
- Phone number: must contain only digits and be 7 to 15 digits long.
- Search and delete: the text typed cannot be empty. Extra spaces are removed with `.strip()`.

## Optional Enhancements Included

- Contacts are displayed in alphabetical order.
- Search supports partial matches and ignores upper/lowercase.

## Challenges and Solutions

- **Challenge:** My first test run showed `IndentationError: unexpected indent`. **Solution:** Since Python treats spaces at the start of a line as purposeful. A hidden space was in front of my `print` line. I copied the line and pasted it in Claude and asked what was wrong. I received the answer of a space was in front of the "print" line which I may not have noticed. I deleted the line, pasted it again so it started at the far left, and the error went away.
- **Challenge:** The Terminal output was longer than the screen. **Solution:** I scrolled and maximized the Terminal to check all of it, then copied the whole run into `interaction_log.txt`.

## Example Interaction Log

See `interaction_log.txt` for a complete test run showing: adding two contacts, a duplicate attempt, an invalid phone number, viewing contacts, a successful and an unsuccessful search, deleting a contact, an invalid menu choice, and exiting.