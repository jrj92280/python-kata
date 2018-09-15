import random

from poker.texas_holdem.display_card import display_card
from poker.texas_holdem.evaluate_hand import evaluate_hand
from poker.texas_holdem.score_hand import score_hand


def print_hand(cards):
    hand = [display_card(card) for card in cards]
    # print(hand)
    return hand

def determine_winner(player_one, player_two):
    if not player_two:
        return player_one
    _winner = score_hand(player_one[2], player_two[2])
    return player_one if _winner == 1 else player_two

player_names = []
player_count = 4

# while player_count <= 0 or player_count >= 10:
#    player_count = int(input("How many players? "))
#    if player_count > 9:
#        print("Maximum of 9 players allowed")

# for player in range(player_count):
#    player_name = input('name:')
#    player_names.append([player_name, []])

player_names.append(["jj", [], []])
player_names.append(["jk", [], []])
player_names.append(["bb", [], []])
player_names.append(["cd", [], []])

# button where ante starts make random

button_index = random.randint(0, player_count-1)
button_player = player_names[button_index]

print('Player with button is: ' + button_player[0])
button_index = player_names

_deck = []
suits = 'SCHD'
for suit_index in range(4):
    suit = suits[suit_index]

    for card_value in range(2, 15):
        _deck.append(suit + str(card_value))

assert 52 == len(_deck)

# game loop

for __ in range(2):
    for player in player_names:
        player[1] = []
        player[2] = []

    deck = _deck.copy()
    random.shuffle(deck)
    cards_needed = 2

    for _ in range(cards_needed):
        for player in player_names:
            card = deck.pop()
            player[1].append(card)

    card = deck.pop()
    deck.pop()

    for player in player_names:
        print(player[0] + ': ' + str(print_hand(player[1])))

    # ante

    burn_card = deck.pop()

    card_1 = deck.pop()
    card_2 = deck.pop()
    card_3 = deck.pop()

    flop = [card_1, card_2, card_3]

    print('The flop is: ' + str(print_hand(flop)))

    # bets

    burn_card_2 = deck.pop()

    flop = flop + [deck.pop()]

    print('Runner is: ' + str(print_hand(flop)))

    # bets

    burn_card_3 = deck.pop()

    flop = flop + [deck.pop()]
    print('River is: ' + str(print_hand(flop)))

    # bets

    hands = []

    for player in player_names:
        player_hand = player[1] + flop
        print("Player name: " + player[0] + ' - ' + str(print_hand(player_hand)))
        eval_hand = evaluate_hand(player_hand)
        print(eval_hand)
        hands.append(eval_hand)
        player[2] = eval_hand

    winning_player = None

    for index, player in enumerate(player_names):
        winning_player = determine_winner(player, winning_player)

        #winner = score_hand(hands[index], hands[index + 1])
        # print(player_names[index][0] + " vs " + player_names[index + 1][0] + " --> " + str(winner))
    # put cards back into the deck
    print("THE WINNER IS! " +winning_player[0])
