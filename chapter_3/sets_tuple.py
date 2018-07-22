vowels = {'a', 'e', 'i', 'o', 'u', 'a', 'a', 'i', 'i'}
print (vowels)

vowels2 = set('aeeiouu')
print(vowels2)
word = 'hello'
u = vowels.union(set(word))
print(u)
u_list = sorted(list(u))
print(u_list)
d = vowels.difference(set(word))
print (d)
i = vowels.intersection(set(word))
print (i)
found = vowels.intersection((set(word)))
for vowel in found:
    print(vowel)
vowels = set('aeiou')
word = input("Provide a word to search for vowels: ")
found = vowels.intersection(set(word))
for vowel in found:
    print(vowel)
