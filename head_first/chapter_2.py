# cup1 = 0
# cup2 = 1
# cup3 = 0
# cup1 = cup1 + 1
# cup2 = cup1 - 1
# cup3 =cup1
# cup1= cup1 * 0
# cup2 = cup3
# cup3 = cup1
# cup1 = cup2 % 1
# cup3 = cup2
# cup2 = cup3 - cup3

#
# word1 = 'ox'
# word2 = 'owl'
# word3 = 'cow'
# word4 = 'sheep'
# word5 = 'files'
# word6 = 'trots'
# word7 = 'runs'
# word8 = 'blue'
# word9 = 'red'
# word10 = 'yellow'
# word9 = ' The ' + word9
# passcode = word8
# passcode = word9
# passcode = passcode + ' f'
# passcode = passcode + word1
# passcode = passcode + " "
# passcode = passcode + word6
# print(passcode)
#
# first = ('somewhere')
# last = ('over the rainbow')
# print(first, last)
#
# temp = first
# first = last
# last = temp
# print(first, last)

# page 110
# colors = ['blue', 'red', 'green', 'purple', 'yellow', 'orange', 'pink', 'brown', 'black', 'cyan', 'moscato']
#
# print({index: color for index, color in enumerate(colors)}[random.randint(0, len(colors) - 1)])
#
# colorsDict = {}
#
# for index, color in enumerate(colors):
#     colorsDict[index] = color
#
# print(colorsDict)
#
# randomColor = random.randint(0, 9)
#
# print(colorsDict[randomColor])

# page 113 infinite loop counter - 1 is correct way
counter = 10

while counter > 0:
    print('Counter is', counter)
    counter = counter + 1
print('Liftoff')
