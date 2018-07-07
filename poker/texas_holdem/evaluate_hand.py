def evaluate_hand(hand):
    return sorted(hand, key=sort_cards, reverse=True)[0:5]


def sort_cards(card):
    return int(card.split(',')[0])
