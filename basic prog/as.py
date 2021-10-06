# function, that replaces all vowels in a string with a specified vowel.
def replace_vowels(string, vowel):
    """
    Replace all vowels in a string with a specified vowel.
    """
    vowels = "aeiouAEIOU"
    new_string = ""
    for i in string:
        if i in vowels:
            new_string += vowel
        else:
            new_string += i
    return new_string
print(replace_vowels("apples and bananas", "u"))