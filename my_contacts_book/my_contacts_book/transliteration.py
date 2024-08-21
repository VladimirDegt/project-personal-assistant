import difflib

TRANS_CYRILLIC_TO_LATIN = {
    
    'й': 'q', 'ц': 'w', 'у': 'e', 'к': 'r', 'е': 't', 'н': 'y', 'г': 'u', 'ш': 'i',
    'щ': 'o', 'з': 'p', 'ф': 'a', 'і': 's', 'в': 'd', 'а': 'f', 'п': 'g', 'р': 'h',
    'о': 'j', 'л': 'k', 'д': 'l', 'я': 'z', 'ч': 'x', 'с': 'c', 'м': 'v', 'и': 'b',
    'т': 'n', 'ь': 'm'
}

def transliterate(text: str) -> str:
    """
    Transliterates Cyrillic text to Latin text.

    Args:
        text (str): The text to transliterate.

    Returns:
        str: The transliterated text.
    """
    return ''.join(TRANS_CYRILLIC_TO_LATIN.get(char, char) for char in text)

def suggest_command(user_input: str, commands: list[str]) -> str:
    """
    Suggests the closest matching command based on user input.

    Args:
        user_input (str): The user input text.
        commands (list[str]): The list of available commands.

    Returns:
        str: The suggested command or '' if no close match is found.
    """
    
    user_input_transliterated = transliterate(user_input)
    closest_matches = difflib.get_close_matches(user_input_transliterated, commands, n=1, cutoff=0.1)
    
    
    if closest_matches:
        return closest_matches[0]
    return ""