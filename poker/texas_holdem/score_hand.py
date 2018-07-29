def score_hand(player_one, player_two):
    if len(player_one) != 7 or len(player_two) != 7:
        raise RuntimeError('invalid hands')

    player_one_high_cards = player_one[0]
    player_two_high_cards = player_two[0]
    player_one_pairs = player_one[1]
    player_two_pairs = player_two[1]

    lp1p = len(player_one_pairs)
    lp2p = len(player_two_pairs)

    if lp1p > lp2p:
        return 1
    elif lp1p < lp2p:
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
