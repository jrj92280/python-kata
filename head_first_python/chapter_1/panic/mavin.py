# aranoid_android = "Marvin"
# letters = list(paranoid_android)
# for char in letters:
#    print('\t', char)


paranoid_android = "marvin, the Paranoid Android"
letters = list(paranoid_android)
for char in letters[:6]:
    print('\t', char)
print()
for char in letters[-7:]:
    print('\t' * 2, char)
print()
for char in letters[12:20]:
    print('\t' * 3, char)
