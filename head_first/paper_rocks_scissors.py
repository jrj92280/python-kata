import random

random_choice = random.randint(0, 2)
if random_choice == 0:
    random_choice = 'Rocks'
elif random_choice == 1:
    random_choice = 'Paper'
else:
    random_choice = 'Scissors'

user_choice = input('rock, paper or scissors? ')
print('You chose', user_choice, 'and the computer chose', random_choice)

choices = ['rock', 'paper', 'scissors']
computer_choice = random.choice(choices)
print(computer_choice)
