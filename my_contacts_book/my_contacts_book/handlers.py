from functools import wraps
from typing import List
from address_book import AddressBook
from birthday import Birthday
from record import Record
from email import Email
from note import Note
from colorama import Fore, Style
from prettytable import PrettyTable
from field import Field


def input_error(func):
    """
    Decorator to handle input errors and return error messages.

    Args:
        func: The function to wrap.

    Returns:
        The wrapped function.
    """

    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError) as e:
            return f"{Fore.YELLOW}Error: {str(e)}{Style.RESET_ALL}"

    return inner


@input_error
def add_contact(args: List[str], book: AddressBook) -> str:
    """
    Adds a contact to the address book.

    Args:
        args (List[str]): The arguments for the command.
        book (AddressBook): The address book instance.

    Returns:
        str: The response message.
    """
    if len(args) < 2:
        raise ValueError("Give me name and phone please.")

    name, phone, *optional_args = args
    name = name.capitalize()
    birthday = optional_args[0] if optional_args else None

    existing_record = book.find(name)
    if existing_record and any(phone == p.value for p in existing_record.phones):
        return f"{Fore.YELLOW}Contact with name {name} and phone {phone} number already exists.{Style.RESET_ALL}"

    if existing_record:
        existing_record.add_phone(phone)
    else:
        record = Record(name)
        record.add_phone(phone)
        if birthday:
            record.add_birthday(birthday)
        book.add_record(record)
        return f"{Fore.GREEN}Contact {name} added.{Style.RESET_ALL}"

    return f"{Fore.GREEN}Contact {name} updated.{Style.RESET_ALL}"


@input_error
def change_contact(args: List[str], book: AddressBook) -> str:
    """
    Changes a phone number for an existing contact or removes a phone number if only two arguments are provided.

    Args:
        args (List[str]): The arguments for the command.
        book (AddressBook): The address book instance.

    Returns:
        str: The response message.
    """
    if len(args) == 3:
        name, old_phone, new_phone = args
        name = name.capitalize()
        record = book.find(name)
        if record:
            record.edit_phone(old_phone, new_phone)
            return f"{Fore.GREEN}Phone number updated.{Style.RESET_ALL}"
        return f"{Fore.YELLOW}Contact {name} not found.{Style.RESET_ALL}"

    elif len(args) == 2:
        name, phone_to_remove = args
        name = name.capitalize()
        record = book.find(name)
        if record:
            if record.find_phone(phone_to_remove):
                record.remove_phone(phone_to_remove)
                return f"{Fore.GREEN}Phone number removed.{Style.RESET_ALL}"
            else:
                return f"{Fore.YELLOW}Phone number not found in the contact {name}.{Style.RESET_ALL}"
        return f"{Fore.YELLOW}Contact {name} not found.{Style.RESET_ALL}"

    else:
        raise ValueError("Give me name, old phone and new phone please or name and phone to remove.")


@input_error
def show_contact(args: List[str], book: AddressBook) -> str:
    """
    Shows the the specified contact.

    Args:
        args (List[str]): The arguments for the command.
        book (AddressBook): The address book instance.

    Returns:
        str: The response message.
    """
    if len(args) != 1:
        raise ValueError("Give me contact name, please.")

    name = args[0].capitalize()
    record = book.find(name)
    if record:
        table = PrettyTable()
        table.field_names = ["Name", "Phones", "Birthday", "Email", "Address"]

        phones = ", ".join([str(phone) for phone in record.phones])
        birthday = record.birthday if record.birthday else "–"
        email = record.email if record.email else "–"
        address = record.address if record.address else "–"

        table.add_row([record.name, phones, birthday, email, address])
        return f"{Fore.GREEN}{table}{Style.RESET_ALL}"
    return f"{Fore.YELLOW}Contact {name} not found.{Style.RESET_ALL}"


@input_error
def delete_contact(args: List[str], book: AddressBook) -> str:
    """
    Deletes a contact from the address book.

    Args:
        args (List[str]): The arguments for the command.
        book (AddressBook): The address book instance.

    Returns:
        str: The response message.
    """
    if len(args) != 1:
        raise ValueError("Give me name, please.")

    name = args[0].capitalize()
    record = book.find(name)
    if record:
        book.delete(name)
        return f"{Fore.GREEN}Contact {name} deleted.{Style.RESET_ALL}"
    return f"{Fore.YELLOW}Contact {name} not found.{Style.RESET_ALL}"


@input_error
def change_name(args: list[str], book: AddressBook) -> str:
    """
    Changes the name of an existing contact.

    Args:
        args (list[str]): The arguments containing the old name and the new name.
        book (AddressBook): The address book instance.

    Returns:
        str: A message indicating the result of the operation.
    """
    if len(args) < 2:
        raise ValueError("Provide the current name and the new name.")

    old_name = args[0].capitalize()
    new_name = args[1].capitalize()

    if old_name not in book:
        return f"{Fore.YELLOW}Contact {old_name} not found.{Style.RESET_ALL}"

    if new_name in book:
        return f"{Fore.YELLOW}Contact with this name {new_name} already exists.{Style.RESET_ALL}"

    contact = book[old_name]
    del book[old_name]
    contact.name = new_name
    book[new_name] = contact
    return f"{Fore.GREEN}Contact name changed from '{old_name}' to '{new_name}'.{Style.RESET_ALL}"


@input_error
def show_phone(args: List[str], book: AddressBook) -> str:
    """
    Shows the phone number for the specified contact.

    Args:
        args (List[str]): The arguments for the command.
        book (AddressBook): The address book instance.

    Returns:
        str: The response message.
    """
    if len(args) != 1:
        raise ValueError("Give me name, please.")

    name = args[0].capitalize()
    record = book.find(name)
    if record:
        table = PrettyTable()
        table.field_names = ["Name", "Phones"]
        phones = ", ".join([str(phone) for phone in record.phones])
        table.add_row([name, phones])
        return f"{Fore.GREEN}{table}{Style.RESET_ALL}"
    return f"{Fore.YELLOW}Contact {name} not found.{Style.RESET_ALL}"


@input_error
def add_birthday(args: List[str], book: AddressBook, action: str) -> str:
    """
    Adds a birthday to the specified contact.

    Args:
        args (List[str]): The arguments for the command.
        book (AddressBook): The address book instance.

    Returns:
        str: The response message.
    """
    if len(args) != 2:
        raise ValueError("Give me name and birthday please.")

    name, birthday = args
    name = name.capitalize()
    record = book.find(name)
    if record:
        record.add_birthday(birthday)
        if(action == 'add-birthday'):
            return f"{Fore.GREEN}Birthday added for {name}.{Style.RESET_ALL}"
        else:
           return f"{Fore.GREEN}{name}`s birthday updated.{Style.RESET_ALL}"
    return f"{Fore.YELLOW}Contact {name} not found.{Style.RESET_ALL}"


@input_error
def show_birthday(args: List[str], book: AddressBook) -> str:
    """
    Shows the birthday for the specified contact.

    Args:
        args (List[str]): The arguments for the command.
        book (AddressBook): The address book instance.

    Returns:
        str: The response message.
    """
    if len(args) != 1:
        raise ValueError("Give me name, please.")

    name = args[0].capitalize()
    record = book.find(name)
    if record:
        table = PrettyTable()
        table.field_names = ["Name", "Birthday"]
        birthday = str(record.birthday) if record.birthday else "No birthday set"
        table.add_row([name, birthday])
        return f"{Fore.GREEN}{table}{Style.RESET_ALL}"
    return f"{Fore.YELLOW}Contact {name} not found.{Style.RESET_ALL}"


@input_error
def birthdays(args: List[str], book: AddressBook) -> str:
    """
    Shows upcoming birthdays within the next 7 days.

    Args:
        args (List[str]): The arguments for the command.
        book (AddressBook): The address book instance.

    Returns:
        str: The response message.
    """
    upcoming_birthdays = book.get_upcoming_birthdays()
    if not upcoming_birthdays:
        return f"{Fore.YELLOW}No birthdays in the next 7 days.{Style.RESET_ALL}"
    table = PrettyTable()
    table.field_names = ["Name", "Birthday", "Phones"]
    for record in upcoming_birthdays:
        phones = ", ".join([str(phone) for phone in record.phones])
        table.add_row([record.name, record.birthday, phones])
    return f"{Fore.GREEN}{table}{Style.RESET_ALL}"


@input_error
def add_email(args: List[str], book: AddressBook, action:str) -> str:
    """
    Add a email to the specified contact.

    Args:
        args (List[str]): The arguments for the command.
        book (AddressBook): The address book instance.

    Returns:
        str: The response message.
    """
    if len(args) != 2:
        raise ValueError("Give me name and email please.")

    name, email = args
    name = name.capitalize()
    record = book.find(name)
    if record:
        record.add_email(email)
        if(action == 'add-email'):
            return f"{Fore.GREEN}Email added for {name}.{Style.RESET_ALL}"
        else:
            return f"{Fore.GREEN}{name}`s email has been changed.{Style.RESET_ALL}"
    return f"{Fore.YELLOW}Contact {name} not found.{Style.RESET_ALL}"


@input_error
def delete_email(args: List[str], book: AddressBook) -> str:
    """
    Deletes an email from the contact.

    Args:
        args (List[str]): The arguments for the command.
        book (AddressBook): The address book instance.

    Returns:
        str: The response message.
    """
    if len(args) != 1:
        raise ValueError("Give me name, please.")
    
    name = args[0].capitalize()
    record = book.find(name)
    if record:
        record.add_email('-')
        return f"{Fore.GREEN}{name}`s email has been deleted.{Style.RESET_ALL}"
    return f"{Fore.YELLOW}Contact {name} not found.{Style.RESET_ALL}"


@input_error
def show_email(args: List[str], book: AddressBook) -> str:
    """
    Shows the email for the specified contact.

    Args:
        args (List[str]): The arguments for the command.
        book (AddressBook): The address book instance.

    Returns:
        str: The response message.
    """
    if len(args) != 1:
        raise ValueError("Give me name, please.")

    name = args[0].capitalize()
    record = book.find(name)
    if record:
        table = PrettyTable()
        table.field_names = ["Name", "Email"]
        email = str(record.email) if record.email else "-"
        table.add_row([name, email])
        return f"{Fore.GREEN}{table}{Style.RESET_ALL}"
    return f"{Fore.YELLOW}CContact {name} not found.{Style.RESET_ALL}"


@input_error
def add_address(args: List[str], book: AddressBook, action:str) -> str:
    """
    Adds an address to the specified contact.

    Args:
        args (List[str]): The arguments for the command.
        book (AddressBook): The address book instance.

    Returns:
        str: The response message.
    """
    if len(args) < 2:
        raise ValueError("Give me name and address please.")

    name, *address_parts = args
    name = name.capitalize()
    address = " ".join(address_parts).title()

    record = book.find(name)
    if record:
        record.add_address(address)
        if(action =='add-address'):
            return f"{Fore.GREEN}Address added for {name}.{Style.RESET_ALL}"
        else:
            return f"{Fore.GREEN}{name}`s address has been changed.{Style.RESET_ALL}"
    return f"{Fore.YELLOW}Contact {name} not found.{Style.RESET_ALL}"


@input_error
def delete_address(args: List[str], book: AddressBook) -> str:
    """
    Deletes a address from the contact.

    Args:
        args (List[str]): The arguments for the command.
        book (AddressBook): The address book instance.

    Returns:
        str: The response message.
    """
    if len(args) != 1:
        raise ValueError("Give me name, please.")
    
    name = args[0].capitalize()
    record = book.find(name)
    if record:
        record.add_address('–')
        return f"{Fore.GREEN}{name}`s address has been deleted.{Style.RESET_ALL}"
    return f"{Fore.YELLOW}Contact {name} not found.{Style.RESET_ALL}"


@input_error
def show_address(args: List[str], book: AddressBook) -> str:
    """
    Shows the email for the specified contact.

    Args:
        args (List[str]): The arguments for the command.
        book (AddressBook): The address book instance.

    Returns:
        str: The response message.
    """
    if len(args) != 1:
        raise ValueError("Give me name, please.")
    
    name = args[0].capitalize()
    record = book.find(name)
    if record:
        table = PrettyTable()
        table.field_names = ["Name", "Address"]
        address = str(record.address) if record.address else "-"
        table.add_row([name, address])
        return f"{Fore.GREEN}{table}{Style.RESET_ALL}"
    return f"{Fore.YELLOW}Contact {name} not found.{Style.RESET_ALL}"

@input_error
def add_note(args: list[str], book: AddressBook) -> str:
    """
    Adds a new note to the specified contact in the address book.

    Args:
        args (list[str]): A list containing the contact name and the note title.
        book (AddressBook): The address book where the contact is stored.

    Returns:
        str: A message indicating the result of the operation.

    Raises:
        ValueError: If the number of arguments provided is not equal to 2.
    """
    if len(args) != 2:
        raise ValueError("Provide the contact name and the note title.")

    name, title_value = args
    record = book.find(name.capitalize())

    if not record:
        return f"{Fore.YELLOW}Error: Contact {name} not found.{Style.RESET_ALL}"

    title_value = title_value.capitalize()

    for note in record.notes:
        if note.title.value == title_value:
            return f"{Fore.YELLOW}Error: Note with title '{title_value}' already exists for {name}.{Style.RESET_ALL}"

    text_value = input("Enter the text of the note: ").strip()
    tag_value = input("Enter the tag for the note: ").strip()

    note = Note(title_value, text_value, tag_value)
    record.add_note(note)

    return f"{Fore.GREEN}Note '{title_value}' added to {name}'s record.{Style.RESET_ALL}"

@input_error
def show_notes(args: list[str], book: AddressBook) -> str:
    """
    Show all notes associated with a contact.

    Args:
        args (list[str]): The arguments for the command. Expected to be the contact's name.
        book (AddressBook): The address book instance.

    Returns:
        str: A string representation of the notes for the contact or an error message.
    """
    if len(args) != 1:
        raise ValueError("Provide the contact name.")

    name = args[0].capitalize()
    record = book.find(name)

    if not record:
        return f"{Fore.YELLOW}Error: Contact {name} not found.{Style.RESET_ALL}"

    if not record.notes:
        return f"{Fore.YELLOW}Contact {name} has no notes.{Style.RESET_ALL}"

    table = PrettyTable()
    table.field_names = ["Title", "Text", "Tag"]

    for note in record.notes:
        table.add_row([note.title, note.text, note.tag])

    return f"{Fore.GREEN}Notes for contact {name}:\n{table}{Style.RESET_ALL}"


@input_error
def change_note(args: list[str], book: AddressBook) -> str:
    """
    Updates the text and tag of an existing note for a specified contact in the address book.

    Args:
        args (list[str]): A list containing the contact name and the note title.
        book (AddressBook): The address book where the contact is stored.

    Returns:
        str: A message indicating the result of the operation.

    Raises:
        ValueError: If the number of arguments provided is not equal to 2.
    """
    if len(args) != 2:
        raise ValueError("Provide the contact name and the note title.")

    name, title_value = args
    record = book.find(name.capitalize())

    if not record:
        return f"{Fore.YELLOW}Error: Contact {name} not found.{Style.RESET_ALL}"
    
    title_value = title_value.capitalize()  

    for note in record.notes:
        if note.title.value == title_value:
            new_text = input("Enter the new text for the note: ").strip()
            new_tag = input("Enter the new tag for the note: ").strip()
            note.text.value = new_text
            note.tag.value = new_tag
            return f"{Fore.GREEN}Note '{title_value}' has been updated for {name}.{Style.RESET_ALL}"

    return f"{Fore.YELLOW}Error: Note with title '{title_value}' not found for {name}.{Style.RESET_ALL}"

@input_error
def delete_note(args: list[str], book: AddressBook) -> str:
    """
    Deletes a note with the specified title from a contact's record in the address book.

    Args:
        args (list[str]): A list containing the contact name and the note title.
        book (AddressBook): The address book where the contact and note are stored.

    Returns:
        str: A message indicating the result of the deletion operation.

    Raises:
        ValueError: If the number of arguments provided is not equal to 2.
    """
    if len(args) != 2:
        raise ValueError("Provide the contact name and the note title.")

    name, title_value = args
    record = book.find(name.capitalize())

    if not record:
        return f"{Fore.YELLOW}Error: Contact {name} not found.{Style.RESET_ALL}"

    title_value = title_value.capitalize()  

    for note in record.notes:
        if note.title.value == title_value:
            record.notes.remove(note)
            return f"{Fore.GREEN}Note '{title_value}' has been deleted from {name}'s record.{Style.RESET_ALL}"

    return f"{Fore.YELLOW}Error: Note with title '{title_value}' not found for {name}.{Style.RESET_ALL}"

@input_error
def show_all_notes(book: AddressBook) -> str:
    """
    Displays all contacts with their corresponding notes in a tabular format.

    Args:
        book (AddressBook): The address book containing the contacts and their notes.

    Returns:
        str: A formatted table of contacts with notes, or a message if no contacts with notes are found.
    """
    table = PrettyTable()
    table.field_names = ["Name", "Title", "Text", "Tag"]

    notes_found = False

    for record in book.values():
        if record.notes: 
            for note in record.notes:
                table.add_row([record.name.value, note.title.value, note.text.value, note.tag.value])
            notes_found = True

    if notes_found:
        return f"{Fore.GREEN}All contacts with notes:\n{table}{Style.RESET_ALL}"
    else:
        return f"{Fore.YELLOW}No contacts with notes found.{Style.RESET_ALL}"
    
@input_error
def show_all_notes_sorted_by_tag(book: AddressBook) -> str:
    """
    Displays all contacts with their corresponding notes, sorted by the note's tag, in a tabular format.

    Args:
        book (AddressBook): The address book containing the contacts and their notes.

    Returns:
        str: A formatted table of contacts with notes sorted by tag, or a message if no contacts with notes are found.
    """
    table = PrettyTable()
    table.field_names = ["Name", "Title", "Text", "Tag"]

    notes_list = []

    for record in book.values():
        if record.notes:  
            for note in record.notes:
                notes_list.append((record.name.value, note.title.value, note.text.value, note.tag.value))

    if not notes_list:
        return f"{Fore.YELLOW}No contacts with notes found.{Style.RESET_ALL}"
 
    notes_list.sort(key=lambda x: x[3].lower())  

    
    for name, title, text, tag in notes_list:
        table.add_row([name, title, text, tag])

    return f"{Fore.GREEN}All contacts with notes (sorted by tag):\n{table}{Style.RESET_ALL}"

@input_error
def find_note_by_title(args: list[str], book: AddressBook) -> str:
    """
    Searches for and displays all notes with a specific title across all contacts in the address book.

    Args:
        args (list[str]): A list containing a single string, the title of the note to search for.
        book (AddressBook): The address book containing the contacts and their notes.

    Returns:
        str: A formatted table of notes with the specified title, or a message if no notes with that title are found.

    Raises:
        ValueError: If the number of arguments is not equal to one (i.e., the title is not provided).
    """
    if len(args) != 1:
       raise ValueError("Provide the title of the note to search.")

    title_value = args[0].capitalize()  
    table = PrettyTable()
    table.field_names = ["Name", "Title", "Text", "Tag"]

    found_notes = []

    for record in book.values():
        for note in record.notes:
            if note.title.value == title_value:
                found_notes.append((record.name.value, note.title.value, note.text.value, note.tag.value))

    if not found_notes:
        return f"{Fore.YELLOW}No notes found with Title '{title_value}'.{Style.RESET_ALL}"

    for name, title, text, tag in found_notes:
        table.add_row([name, title, text, tag])

    return f"{Fore.GREEN}Notes with Title '{title_value}':\n{table}{Style.RESET_ALL}"

@input_error
def find_note_by_tag(args: list[str], book: AddressBook) -> str:
    """
    Searches for and displays all notes with a specific tag across all contacts in the address book.

    Args:
        args (list[str]): A list containing a single string, the tag of the note to search for.
        book (AddressBook): The address book containing the contacts and their notes.

    Returns:
        str: A formatted table of notes with the specified tag, or a message if no notes with that tag are found.

    Raises:
        ValueError: If the number of arguments is not equal to one (i.e., the tag is not provided).
    """
    if len(args) != 1:
        raise ValueError("Provide the tag of the note to search.")

    tag_value = args[0].lower()
    table = PrettyTable()
    table.field_names = ["Name", "Title", "Text", "Tag"]

    found_notes = []

    for record in book.values():
        for note in record.notes:
            if note.tag.value.lower() == tag_value:
                found_notes.append((record.name.value, note.title.value, note.text.value, note.tag.value))

    if not found_notes:
        return f"{Fore.YELLOW}No notes found with Tag '{tag_value}'.{Style.RESET_ALL}"

    for name, title, text, tag in found_notes:
        table.add_row([name, title, text, tag])

    return f"{Fore.GREEN}Notes with Tag '{tag_value}':\n{table}{Style.RESET_ALL}"


@input_error
def show_all(book: AddressBook) -> str:
    """
    Shows all contacts in the address book.

    Args:
        book (AddressBook): The address book instance.

    Returns:
        str: The response message.
    """
    if not book:
        return f"{Fore.YELLOW}The address book is empty.{Style.RESET_ALL}"

    table = PrettyTable()
    table.field_names = ["Name", "Phones", "Birthday", "Email", "Address"]
    for name, record in book.data.items():
        phones = ", ".join([str(phone) for phone in record.phones])
        birthday = str(record.birthday) if record.birthday else "–"
        email = str(record.email) if record.email else "–"
        address = str(record.address) if hasattr(record, 'address') and record.address else "–"
        table.add_row([record.name, phones, birthday, email, address])
    return f"{Fore.GREEN}{table}{Style.RESET_ALL}"