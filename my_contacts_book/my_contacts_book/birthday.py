from datetime import datetime
from field import Field

class Birthday(Field):
    """
    Class to represent a birthday field.

    Attributes:
        value (str): The birthday value in DD.MM.YYYY format.
    """

    def __init__(self, value: str):
        """
        Initializes a Birthday instance.

        Args:
            value (str): The birthday value in DD.MM.YYYY format.
        """
        self.value = self.validate_birthday(value)

    def validate_birthday(self, value: str) -> str:
        """
        Validates and parses the birthday value.

        Args:
            value (str): The birthday value in DD.MM.YYYY format.

        Returns:
            str: The validated birthday value.

        Raises:
            ValueError: If the birthday value is not in the correct format.
        """
        try:
            datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        return value