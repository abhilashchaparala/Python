# Function to sort Python Dictionaries by Key

def sort_dictionaries(dictionary):
    """
    Sorts a dictionary by its keys.
    """
    return sorted(dictionary.items(), key=lambda x: x[0])
# Function to sort Python Dictionaries by value

def sort_dictionaries_by_value(dictionary):
    """
    Sorts a dictionary by its values.
    """
    return sorted(dictionary.items(), key=lambda x: x[1])
# Function to sort Python Dictionaries by Key and Value
