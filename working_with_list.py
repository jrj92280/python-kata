vowels = ['a', 'e', 'i', 'o', 'u']

words = [
    'milliways', 'hitch_hiker', 'galaxy', 'sky',
    'milliways', 'hitch_hiker', 'galaxy', 'sky',
    'milliways', 'hitch_hiker', 'galaxy', 'sky',
    'jason', 'dog'
]

print(words)

found = []
found_words = []
found_words_set = set()
found_words_dict = dict()

for word in words:
    if word in found_words_dict:
        found_words_dict[word] = found_words_dict[word] + 1
    else:
        found_words_dict[word] = 1

print(found_words_dict)

for key in found_words_dict:
    if found_words_dict[key] == 1:
        print(key)


for word in words:
    # words
    if word not in found_words:
        found_words.append(word)

    # set
    found_words_set.add(word)

    # vowels
    for letter in word:
        if letter in vowels:
            if letter not in found:
                found.append(letter)

for vowel in found:
    print(vowel)

for word in found_words:
    print(word)

for word in found_words_set:
    print(word)
