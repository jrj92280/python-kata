def search4vowels(pharse :str) -> set:
    """"Return any vowels found in a supplied word."""
    vowels = set('aeiou')
    return vowels.intersection(set(pharse))


print(search4vowels('hitch-hiker'))
print(search4vowels('life, the universe and everything'))
print(search4vowels('sky'))
print(search4vowels('galaxy'))

# '''list'''
#
# l = list()
# print(l)
# l = [1, 2, 3]
# print(l)
#
# '''dictionary'''
#
# d = dict()
# print(d)
# d = {'first': 1, 'second': 2, 'third': 3}
# print(d)
#
# '''set'''
#
# s = set()
# print(s)
# s = {1, 2, 3}
# print(s)
#
# '''tuple'''
#
# t = tuple()
# print(t)
# t = (1, 2, 3)
# print(t)
#
