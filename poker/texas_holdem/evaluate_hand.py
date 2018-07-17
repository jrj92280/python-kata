from collections import defaultdict


def evaluate_hand(hand):
    card_groups = create_groups(hand)

    sorted_cards = sorted(hand, key=sort_cards, reverse=True)

    high_cards = sorted_cards[0:5]
    pairs = group_cards(2, card_groups, hand)
    three_of_kinds = group_cards(3, card_groups, hand)
    four_of_kind = group_cards(4, card_groups, hand)
    full_house = get_full_house(pairs, three_of_kinds)
    straight = get_straight(sorted_cards)

    flush = []
    suits = defaultdict(list)

    for card in sorted_cards:
        suit = get_suit_value(card)
        suits[suit].append(card)
    for suit, cards in suits.items():
        if len(cards) >= 5:
            flush = cards

    return [high_cards, pairs, three_of_kinds, four_of_kind, full_house, straight, flush]


def get_straight(sorted_cards):
    straight = []
    last_card_value = None
    ace_card = None

    for card in sorted_cards:
        card_value = get_card_value(card)
        if card_value == 14:
            ace_card = card

        if card_value + 1 == last_card_value:
            straight.append(card)
        elif card_value != last_card_value and len(straight) < 4:
            straight = [card]
        else:
            continue

        last_card_value = card_value

    if len(straight) == 4 and ace_card and get_card_value(straight[3]) == 2:
        straight.append(ace_card)
    elif len(straight) < 5:
        straight = []

    return straight


def create_groups(hand):
    same_cards = defaultdict(int)
    for card in hand:
        card_value = get_card_value(card)
        same_cards[card_value] += 1
    return same_cards


def group_cards(group_count, card_groups, hand):
    groups = []

    for card_value, card_count in card_groups.items():
        if card_count == group_count:
            group = []
            for card in hand:
                if get_card_value(card) == card_value:
                    group.append(card)
            groups.append(group)

    return groups


def sort_cards(card):
    return get_card_value(card)


def get_card_value(card):
    return int(card[1:])


def get_suit_value(card):
    return card[0]


def get_full_house(pairs, three_of_kinds):
    full_house = []
    if len(pairs) and len(three_of_kinds):
        full_house.extend(three_of_kinds[0])
        # ps
        pairs_index = 0
        if len(pairs) == 2 and get_card_value(pairs[0][0]) < get_card_value(pairs[1][0]):
            pairs_index = 1
        full_house.extend(pairs[pairs_index])
    return full_house
