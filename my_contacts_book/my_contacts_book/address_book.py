from collections import UserDict
from typing import List, Optional
from record import Record
from datetime import datetime, timedelta


class AddressBook(UserDict):
    """
    Class to represent an address book.

    Methods:
        add_record(record): Adds a record to the address book.
        find(name): Finds a record by name.
        delete(name): Deletes a record by name.
        get_upcoming_birthdays(): Gets contacts with upcoming birthdays within the next 7 days.
    """

    def add_record(self, record: Record) -> None:
        """
        Adds a record to the address book.

        Args:
            record (Record): The record to add.
        """
        if record.name.value in self.data:
            print(f"Contact {record.name} already exists.")
        else:
            self.data[record.name.value] = record

    def find(self, name: str) -> Optional[Record]:
        """
        Finds a record by name.

        Args:
            name (str): The name to find.

        Returns:
            Optional[Record]: The found record, or None if not found.
        """
        return self.data.get(name, None)

    def delete(self, name: str) -> None:
        """
        Deletes a record by name.

        Args:
            name (str): The name of the record to delete.
        """
        if name in self.data:
            del self.data[name]
        else:
            print(f"Contact {name} not found.")

    def get_upcoming_birthdays(self) -> List[Record]:
        """
        Gets contacts with upcoming birthdays within the next 7 days.

        Returns:
            List[Record]: A list of records with upcoming birthdays.
        """
        today = datetime.today()
        upcoming_birthdays = []
        for record in self.data.values():
            if record.birthday:
                birthday = datetime.strptime(record.birthday.value, "%d.%m.%Y")
                birthday = birthday.replace(year=today.year)
                if today <= birthday <= today + timedelta(days=7):
                    upcoming_birthdays.append(record)
        return upcoming_birthdays
