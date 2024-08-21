from field import Field
class Note:
    """
    Class to represent a note.

    Attributes:
        title (Field): The title of the note.
        text (Field): The text content of the note.
        tag (Field): The tag associated with the note.
    """

    def __init__(self, title: str, text: str, tag: str) -> None:
        """
        Initializes a Note instance.

        Args:
            title (str): The title of the note.
            text (str): The text content of the note.
            tag (str): The tag associated with the note.
        """
        self.title = Field(title)
        self.text = Field(text)
        self.tag = Field(tag)

    def __str__(self) -> str:
        """
        Returns a string representation of the note.

        Returns:
            str: The string representation of the note.
        """
        return f"Title: {self.title}, Text: {self.text}, Tag: {self.tag}"