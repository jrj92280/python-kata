import random

from poker.texas_holdem.display_card import display_card
from poker.texas_holdem.evaluate_hand import evaluate_hand
from poker.texas_holdem.score_hand import score_hand


def print_hand(cards):
    hand = [display_card(card) for card in cards]
    print(hand)
    return hand


player_names = []

player_count = 2  # int(input("How many players? "))

# for player in range(player_count):
#     player_name = input('name:')
#     player_names.append([player_name, []])
player_names.append(["jj", []])
player_names.append(["jk", []])
# button where ante starts make random
deck = []
suits = 'SCHD'
for suit_index in range(4):
    suit = suits[suit_index]

    for card_value in range(2, 15):
        deck.append(suit + str(card_value))

assert 52 == len(deck)

# game loop

random.shuffle(deck)

cards_needed = 2

for _ in range(cards_needed):
    for player in player_names:
        card = deck.pop()
        player[1].append(card)


card = deck.pop()
deck.pop()

for player in player_names:
    print(player[0])
    print_hand(player[1])

# ante

burn_card = deck.pop()

card_1 = deck.pop()
card_2 = deck.pop()
card_3 = deck.pop()

flop = [card_1, card_2, card_3]

print('The flop is')
print_hand(flop)

# bets

burn_card_2 = deck.pop()

flop = flop + [deck.pop()]

print('Runner is')
print_hand(flop)

# bets

burn_card_3 = deck.pop()

flop = flop + [deck.pop()]
print('River is')
print_hand(flop)

# bets

hands = []

for player in player_names:
    player_hand = player[1] + flop
    print("Player name: " + player[0])
    print_hand(player_hand)

    eval_hand = evaluate_hand(player_hand)
    print(eval_hand)
    hands.append(eval_hand)

print("!!!!!")
print(score_hand(hands[0], hands[1]))
# put cards back into the deck
