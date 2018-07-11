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