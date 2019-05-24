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

# def make_sundae(ice_cream='vanilla', sauce='chocolate', nuts=True, banana=True, brownies=False, whipped_cream=True):
#     recipe = ice_cream + 'ice cream and ' + sauce + 'sauce'
#     if nuts:
#         recipe = recipe + 'with nuts and '
#     if banana:
#         recipe = recipe + 'a banana and'
#     if brownies:
#         recipe = recipe + 'a brownie and '
#     if not whipped_cream:
#         recipe = recipe + 'no '
#     recipe = recipe + 'whipped cream on top.'
#     return recipe
#
#
# sundae = make_sundae()
# print('One sundae coming up with', sundae)
#
# sundae = make_sundae('chocolate')
# print('One sundae coming up with', sundae)
#
# sundae = make_sundae(sauce='caramel', whipped_cream=False, banana=False)
# print('One sundae coming up with', sundae)
#
# sundae = make_sundae(whipped_cream=False, banana=True, brownies=True, ice_cream='peanut butter')
# print('One sundae coming up with', sundae)

# // page 215///
#
# balance = 10500
# camera_on = True
#
#
# def steal(balance, amount):
#     global camera_on
#     camera_on = False
#
#     if (amount < balance):
#         balance = balance - amount
#         return amount
#         camera_on = True
#
#
# proceeds = steal(balance, 1250)
# print('Criminal:  you stole', proceeds)
