phrase = "don't panic!"
plist = list(phrase)
print (phrase)
print (plist)
plist.pop(0)
plist.pop(2)
plist.pop(6);plist.pop(6);plist.pop(6)
plist.insert(2,plist.pop(3))
plist.insert(4,plist.pop(5))
plist.remove("!")
new_phrase = ''.join(plist)

print (plist)
print (new_phrase)