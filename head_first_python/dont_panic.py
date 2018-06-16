phrase = "don't panic!"
plist = list(phrase)

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)

new_phrase = ''.join(plist[1:3])
new_phrase = new_phrase + ''.join([plist[5], plist[4], plist[7], plist[6]])
print(plist)
print(new_phrase)
