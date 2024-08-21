import re
from field import Field


class Email(Field):
    def __init__(self, email: str):
        """
        Initializes the Email field with a validated email address.

        :param email: The email address to validate and store.
        :raises ValueError: If the email does not meet validation criteria.
        """
        self.value = self.validate_email(email)

    def validate_email(self, email: str) -> str:
        """
        Validates the provided email address based on the following rules:
        - Minimum of 3 characters and a maximum of 150 characters.
        - Must be in a valid email format.
        - Should not contain the ".ru" domain.

        :param email: The email address to validate.
        :return: The validated email address.
        :raises ValueError: If the email does not meet the validation criteria.
        """
        if email == '-':
            return email

        if len(email) < 3 or len(email) > 150:
            raise ValueError("Email must be between 3 and 150 characters long.")

        email_pattern = re.compile(
            r"^[A-Z0-9._%+-]+@(?!.*\.ru)[A-Z0-9.-]+\.[A-Z]{2,4}$", re.IGNORECASE
        )

        if not email_pattern.match(email):
            raise ValueError("Invalid email format or contains forbidden domain.")

        return email
