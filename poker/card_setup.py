import itertools
import random

player_count = int(input("How many players? "))

player_names = []

for player in range(player_count):
    player_name = input('name:')
    player_names.append(player_name)


cards = ['A, spades', 'A, clubs', 'A, hearts', 'A, dimonds',
         'K, spades', 'K, clubs', 'K, hearts', 'K, dimonds',
         'Q, spades', 'Q, clubs', 'Q, hearts', 'Q, dimonds',
         'J, spades', 'J, clubs', 'J, hearts', 'J, dimonds',
         '10, spades', '10, clubs', '10, hearts', '10, dimonds',
         '9, spades', '9, clubs', '9, hearts', '9, dimonds',
         '8, spades', '8, clubs', '8, hearts', '8, dimonds',
         '7, spades', '7, clubs', '7, hearts', '7, dimonds',
         '6, spades', '6, clubs', '6, hearts', '6, dimonds',
         '5, spades', '5, clubs', '5, hearts', '5, dimonds',
         '4, spades', '4, clubs', '4, hearts', '4, dimonds',
         '3, spades', '3, clubs', '3, hearts', '3, dimonds',
         '2, spades', '2, clubs', '2, hearts', '2, dimonds']

cards_needed = 2

random.shuffle(cards)
cards.pop(-1)
for card in cards[:cards_needed]:
        print(card)


