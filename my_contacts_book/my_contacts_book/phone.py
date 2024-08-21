import re
from field import Field

class Phone(Field):
    def __init__(self, number: str):
        self.value = self.validate_phone(number)

    def validate_phone(self, number: str) -> str:
        """
        Validate the phone number to ensure it contains exactly 10 digits.
        
        Args:
            number (str): The phone number to validate.
        
        Returns:
            str: The validated phone number.
        
        Raises:
            ValueError: If the phone number is not exactly 10 digits.
        """
        if not re.match(r"^\d{10}$", number.strip()):
            raise ValueError("Phone number should contain exactly 10 digits.")

        return number