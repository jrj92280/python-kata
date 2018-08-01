def search4vowels(word):
    """"Display any vowels found in an asked - for word."""
    vowels = set('aeiou')
    found = vowels.intersection(set(word))
    return bool(found)

print(search4vowels('hitch-hiker'))
