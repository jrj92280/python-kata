from collections import defaultdict


def evaluate_hand(hand):
    card_groups = create_groups(hand)

    high_cards = sorted(hand, key=sort_cards, reverse=True)[0:5]
    pairs = group_cards(2, card_groups, hand)
    three_of_kinds = group_cards(3, card_groups, hand)
    four_of_kind = group_cards(4, card_groups, hand)
    full_house = []

    if len(pairs) and len(three_of_kinds):
        full_house.extend(three_of_kinds[0])
        # ps
        pairs_index = 0
        if len(pairs) == 2 and get_card_value(pairs[0][0]) < get_card_value(pairs[1][0]):
            pairs_index = 1
        full_house.extend(pairs[pairs_index])

    return [high_cards, pairs, three_of_kinds, four_of_kind, full_house]


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
    return int(card.split(',')[0])
