def search4vowels(word):
    """"Return any vowels found in a supplied word."""
    vowels = set('aeiou')
    return vowels.intersection(set(word))


print(search4vowels('hitch-hiker'))
print(search4vowels('life, the universe and everything'))
print(search4vowels('sky'))
print(search4vowels('galaxy'))