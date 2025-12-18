# helpers.py

def clean_input(user_input):
    """
    Cleans and normalizes user input.
    - Trims extra spaces
    - Converts to lowercase
    """
    return user_input.strip().lower()
