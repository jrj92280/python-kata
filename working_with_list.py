vowels = ['a', 'e', 'i', 'o', 'u']

words = [
    'milliways', 'hitch_hiker', 'galaxy', 'sky',
    'milliways', 'hitch_hiker', 'galaxy', 'sky',
    'milliways', 'hitch_hiker', 'galaxy', 'sky'
]

print(words)

found = []
found_words = []
found_words_set = set()

for word in words:
    # words
    if word not in found_words:
        found_words.append(word)

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
