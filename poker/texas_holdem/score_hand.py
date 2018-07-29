from poker.texas_holdem.evaluate_hand import get_card_value

def score_hand(player_one, player_two):
    if len(player_one) != 7 or len(player_two) != 7:
        raise RuntimeError('invalid hands')

    player_one_high_cards = player_one[0]
    player_two_high_cards = player_two[0]
    player_one_pairs = player_one[1]
    player_two_pairs = player_two[1]

    lp1p = len(player_one_pairs)
    lp2p = len(player_two_pairs)

    if lp1p != 0 and lp2p == 0:
        return 1
    elif lp1p == 0 and lp2p != 0:
        return -1
    elif lp1p != 0 and lp2p != 0:
        print("We have a pair")

        while lp1p != lp2p:
            if lp1p > lp2p:
                player_two_pairs.append([])
                lp2p += 1
            else:
                player_one_pairs.append([])
                lp1p += 1

        p1h = None
        p2h = None

        for player_one_pair, player_two_pair in zip(player_one_pairs, player_two_pairs):
            print(player_one_pair, player_two_pair)

            p1c = get_card_value(player_one_pair[0]) if len(player_one_pair) else 0
            p2c = get_card_value(player_two_pair[0]) if len(player_two_pair) else 0

            p1h = p1h or p1c
            p2h = p2h or p2c

            if p1h != p1c:
                p1h = p1h if p1h > p1c else p1c
            if p2h != p2c:
                p2h = p2h if p2h > p2c else p2c

        print(p1h, p2h)

        if p1h > p2h:
            return 1
        elif p1h < p2h:
            return -1


    for player_one_card, player_two_card in zip(player_one_high_cards, player_two_high_cards):
        player_one_card_value = get_card_value(player_one_card)
        player_two_card_value = get_card_value(player_two_card)

        if player_one_card_value == player_two_card_value:
            continue
        elif player_one_card_value > player_two_card_value:
            return 1
        else:
            return -1

    return 0


def get_card_value(card):
    return int(card[1:])
