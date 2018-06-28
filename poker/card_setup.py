import itertools
import random

player_count = int(input("How many players? "))

player_names = []

for player in range(player_count):
    player_name = input('name:')
    player_names.append(player_name)
    player_hand = player_hand

cards = ['A, spades', 'A, clubs', 'A, hearts', 'A, diamonds',
         'K, spades', 'K, clubs', 'K, hearts', 'K, diamonds',
         'Q, spades', 'Q, clubs', 'Q, hearts', 'Q, diamonds',
         'J, spades', 'J, clubs', 'J, hearts', 'J, diamonds',
         '10, spades', '10, clubs', '10, hearts', '10, diamonds',
         '9, spades', '9, clubs', '9, hearts', '9, diamonds',
         '8, spades', '8, clubs', '8, hearts', '8, diamonds',
         '7, spades', '7, clubs', '7, hearts', '7, diamonds',
         '6, spades', '6, clubs', '6, hearts', '6, diamonds',
         '5, spades', '5, clubs', '5, hearts', '5, diamonds',
         '4, spades', '4, clubs', '4, hearts', '4, diamonds',
         '3, spades', '3, clubs', '3, hearts', '3, diamonds',
         '2, spades', '2, clubs', '2, hearts', '2, diamonds']

deck = set(itertools.product(cards))
drawn_cards = random.sample(deck, (5 + 2 * player_count))

players = []

random.shuffle(cards)
player_hand = player_hand
print (cards)
player_hand = player_hand
