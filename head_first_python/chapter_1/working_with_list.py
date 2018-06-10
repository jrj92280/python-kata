vowels = ['a', 'e', 'i', 'o', 'u']

words = [
    'milliways', 'hitch_hiker', 'galaxy', 'sky',
]

print(words)

found = []


for word in words:
    for letter in word:
        if letter in vowels:
            if letter not in found:
                found.append(letter)

for vowel in found:
    print(vowel)
