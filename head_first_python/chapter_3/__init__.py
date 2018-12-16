
#fruits  = {}
#fruits['apples'] = 10
#fruits
#'apples : 10'
#'apples'in fruits
#if 'pears' not in fruits:
#    fruits['pears'] = 0
#fruits['pears'] += 1
#fruits


#if 'bananas' in fruits:
 #   fruits['bananas'] += 1
#else:
#    fruits['bananas'] = 1

#fruits
#{'bananas': 2,
# 'pears':2,
##': 10}

vowels = ['a', 'e', 'i', 'o', 'u']
word = input('Provide a word to search for vowels: ')

found = {}

for letter in word:
    if letter in vowels:
        found.setdefault(letter, 0)
        found[letter] += 1

for k, v in sorted(found.items()):
    print(k, 'was found', v, 'time(s). ')

