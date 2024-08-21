# A Comprehensive Address Book Application

This application is your ultimate personal assistant, helping you manage contacts, birthdays, addresses, and notes effortlessly. With a clean interface and robust functionality, it ensures you never lose touch with important details.

---

# Keep Your Contacts Organized

Manage your contacts efficiently with our address book application. From phone numbers and emails to addresses and personalized notes, keep everything in one place. Easily search, edit, and organize your data with intuitive commands.

---

# Stay Ahead of Important Dates

Never miss a birthday again! This application not only helps you manage contact information but also tracks upcoming birthdays, ensuring you're always prepared to celebrate with your loved ones.

---

# Personalized Notes at Your Fingertips

Add, edit, and delete notes linked to your contacts. Whether it's a quick reminder or important information, your notes are always just a command away. Plus, sort and find notes by title or tag for easy access.

---

# Effortless Navigation and Control

With a wide range of commands, from adding contacts to searching notes, this application puts you in full control. Designed for simplicity and efficiency, it’s perfect for anyone looking to streamline their contact management.

---

# Your Digital Rolodex Reimagined

Bringing a modern twist to the classic address book, this application is more than just a contact list. It’s a powerful tool for managing all aspects of your personal and professional connections, ensuring you stay organized and connected.

## Installation

To install the package, you can use pip:

```sh
pip install my_contacts_book_bot

Usage
Once installed, you can run the bot using the following command:

my_contacts_book

Commands
hello: Displays a greeting message.
help: Shows this help message.
add <name> <phone>: Adds a new contact with the specified name and phone number.
                    If the contact already exists but with a different number, the contact will be updated.
change <name> <old_phone> <new_phone>: Changes the phone number for an existing contact.
                                        If only the name and the existing number are provided, the number will be removed.
change-name <old_name> <new_name>: Changes the name of an existing contact.
phone <name>: Shows the phone number for the specified contact.
contact <name>: Shows the the specified contact.
delete <name>: Deletes a contact from the address book.
add-birthday <name> <birthday>: Adds a birthday to the specified contact.
change-birthday <name> <new_birthday>: Changes the birthday for an existing contact.
show-birthday <name>: Shows the birthday for the specified contact.
birthdays: Shows upcoming birthdays within the next 7 days.
add-email <name> <email>: Add an email to the specified contact.
change-email <name> <new email>: Change an email to the specified contact.
show-email <name>:  Shows the email for the specified contact.
delete-email <name> <email>: Delete an email to the specified contact.
add-address <name> <address>: Adds an address to the specified contact.
change-address <name> <new address>: Change an address to the specified contact.
show-address <name>:  Shows the address for the specified contact.
delete-address <name>: Delete an address to the specified contact.
add-note <name> <title>: Adds a new note.
change-note <name> <title>: Changes the note for the specified contact.
delete-note <name> <title>: Delete the note for the specified contact.
show-notes <name>: Shows the notes for the specified contact.
show-all-notes: Shows all notes with their tags.
show-all-notes-sorted-by-tag: Shows all notes sorted by their tags.
find-note-by-title <title. Finds a notes by tytle.
find-note-by-tag <tag. Finds a notes by tag.
all: Shows all contacts with their phone numbers.
close / exit / bye: Exits the program.

```

## Persistent Storage

The bot automatically saves your address book to disk when you exit the program and restores it when you start the program again. This means you won't lose your contacts between sessions.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

```

```
