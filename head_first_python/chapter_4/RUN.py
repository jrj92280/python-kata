import string

def search4letters(pharse: str) -> set:
    """"Return any letters found in a supplied word."""
    letter = set(string.ascii_letters)
    return_value = sorted(letter.intersection(set(pharse)))
    return return_value


search4letters =  print(search4letters)

