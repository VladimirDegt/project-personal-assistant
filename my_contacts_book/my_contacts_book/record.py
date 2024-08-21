from typing import List, Optional
from name import Name
from phone import Phone
from birthday import Birthday
from email import Email
from address import Address
from note import Note

class Record:
    """
    Class to represent a record in the address book.

    Attributes:
        name (Name): The name of the contact.
        phones (List[Phone]): The list of phone numbers associated with the contact.
        birthday (Optional[Birthday]): The birthday of the contact.
        email (Optional[Email]): The email address of the contact.
        address (Optional[Address]): The address of the contact.
        notes (Optional[List[Note]]): The optional list of notes associated with the contact.
    """

    def __init__(self, name: str) -> None:
        """
        Initializes a Record instance.

        Args:
            name (str): The name of the contact.
        """
        self.name = Name(name)
        self.phones: List[Phone] = []
        self.birthday: Optional[Birthday] = None
        self.email: Optional[Email] = None
        self.address: Optional[Address] = None
        self.notes: Optional[List[Note]] = []

    
    def add_phone(self, phone: str) -> None:
        """
        Adds a phone number to the contact.

        Args:
            phone (str): The phone number to add.
        """
        self.phones.append(Phone(phone))

    def remove_phone(self, phone: str) -> None:
        """
        Removes a phone number from the contact.

        Args:
            phone (str): The phone number to remove.
        """
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone: str, new_phone: str) -> None:
        """
        Edits a phone number in the contact.

        Args:
            old_phone (str): The old phone number to be replaced.
            new_phone (str): The new phone number to replace the old one.
        """
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone

    def find_phone(self, phone: str) -> Optional[Phone]:
        """
        Finds a phone number in the contact.

        Args:
            phone (str): The phone number to find.

        Returns:
            Optional[Phone]: The phone number if found, otherwise None.
        """
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def add_birthday(self, birthday: str) -> None:
        """
        Adds a birthday to the contact.

        Args:
            birthday (str): The birthday value in DD.MM.YYYY format.
        """
        self.birthday = Birthday(birthday)

    def add_email(self, email) -> None:
        """
        Add an email to the contact

        Args:
        email(str): The email value example@example.com format
        """
        self.email = Email(email)
        
    def add_address(self, address: str) -> None:
        """
        Adds an address to the contact.

        Args:
            address (str): The address as a string.
        """
        self.address = Address(address)
        
    def add_note(self, note: Note) -> None:
            self.notes.append(note)

    def __str__(self) -> str:
        """
        Returns a string representation of the contact.

        Returns:
            str: The string representation of the contact.
        """
        phones = ", ".join([str(phone) for phone in self.phones])
        birthday = f", Birthday: {self.birthday}" if self.birthday else ""
        address = f", Address: {self.address}" if self.address else ""
        email = f", Email: {self.email}" if self.email else ""
        notes = ", ".join([str(note) for note in self.notes])
        notes_str = f", Notes: {notes}" if notes else ""
        return f"Name: {self.name}, Phones: {phones}{birthday}{email}{address}{notes_str}"