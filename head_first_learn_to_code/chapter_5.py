# print("Get those dogs ready")
#
# def bark(name, weight):
#     if weight > 20:
#         print(name, "says WOOF WOOF")
#     else:
#         print(name, 'says woof woof')
#
#
# bark('Cody', 40)
# bark('Sparky', 9)
# bark('Jackson', 12)
# bark('Fido', 65)
# bark('Speedy', 20)
# bark('Barnaby', -1)
# bark('Scottie', 0)
# bark('Lady', 20)
# bark('Spot', 10)
# bark('Rover', 21)
#
# print("Okay, we're all done")

# ///page 191///
# def how_should_I_get_there(miles):
#     if miles > 120:
#         print('Take a plane')
#     elif miles >= (2):
#         print('Take a car')
#     else:
#         print('Walk')
#
#
# how_should_I_get_there(800.3)
# how_should_I_get_there(2)
# how_should_I_get_there(.5)


# // page 201 //

# def drink_me(param):
#     msg = 'Drinking ' + param + ' glass'
#     print(msg)
#     param = 'empty'
#
#
# glass = 'full'
# drink_me(glass)
# print('The glass is', glass)

# ///Page 207 ///
#
# greeting = 'Greeetings'
#
#
# def greet(name, message):
#     global greeting
#     greeting = 'Hi'
#     print(greeting, name + '.', message)
#
#
# greet('June', 'See you soon!')
# print(greeting)

# ///page 210///
def greet(name, emoticon, message='You rule!'):
    print('Hi', name + '.', message, emoticon)

#
# ///greet(name, emoticons, meassage='You rule!'):///// runs error//
# greet(message='Where have you been?', name='Jill', emoticons='thumbs up')
# greet('Betty', message= 'Yo!', emoticon':)')

greet(message='Where have you been?', name='Jill', emoticon='thumbs up')

greet('Betty', message='YO', emoticon=':)')
