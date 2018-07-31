def score_hand(player_one: list, player_two: list):
    if len(player_one) != 7 or len(player_two) != 7:
        raise RuntimeError('invalid hands')

    player_one_pairs = player_one[1]
    player_two_pairs = player_two[1]

    player_one_has_pairs = len(player_one_pairs)
    player_two_has_pairs = len(player_two_pairs)

    if player_one_has_pairs and not player_two_has_pairs:
        return 1
    elif not player_one_has_pairs and player_two_has_pairs:
        return -1
    elif player_one_has_pairs and player_two_has_pairs:
        make_list_same_size(player_one_pairs, player_two_pairs)

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

    player_one_high_cards = player_one[0]
    player_two_high_cards = player_two[0]

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


def make_list_same_size(list_one: list, list_two: list) -> None:
    length_list_one = len(list_one)
    length_list_two = len(list_two)

    while length_list_one != length_list_two:
        if length_list_one > length_list_two:
            list_two.append([])
            length_list_two += 1
        else:
            list_one.append([])
            length_list_one += 1


def get_card_value(card):
    return int(card[1:])
