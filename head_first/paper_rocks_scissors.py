import random

computer_choice = random.randint(0, 2)
if computer_choice == 0:
    computer_choice = 'rock'
elif computer_choice == 1:
    computer_choice = 'paper'
else:
    computer_choice = 'scissors'

user_choice = input('rock, paper or scissors? ')
# print('You chose', user_choice, 'and the computer chose', computer_choice)

# choices = ['rock', 'paper', 'scissors']
# computer_choice = random.choice(choices)
# print(computer_choice)

winner = ('tie', 'user', 'computer')
if computer_choice == user_choice:
    winner = 'tie'
elif computer_choice == 'rock' and user_choice == 'scissors':
    winner = 'computer'
elif computer_choice == 'paper' and user_choice == 'rock':
    winner = 'computer'
elif computer_choice == 'scissors' and user_choice == 'paper':
    winner = 'computer'
else:
    winner = 'user'

print('The winner is', winner)
