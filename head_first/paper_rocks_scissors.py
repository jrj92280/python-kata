import random

random_choice = random.randint(0, 2)
if random_choice == 0:
    random_choice = 'Rocks'
elif random_choice == 1:
    random_choice = 'Paper'
else:
    random_choice = 'Scissors'

print('The computer chooses', random_choice)
