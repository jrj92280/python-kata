from collections import defaultdict


def evaluate_hand(hand):
    same_cards = defaultdict(int)

    for card in hand:
        card_value = get_card_value(card)
        same_cards[card_value] += 1

    pairs = []
    for card_value, card_count in same_cards.items():
        if card_count == 2:
            pair = []
            for card in hand:
                if get_card_value(card) == card_value:
                    pair.append(card)
            pairs.append(pair)

    high_cards = sorted(hand, key=sort_cards, reverse=True)[0:5]
    return [high_cards, pairs]


def sort_cards(card):
    return get_card_value(card)


def get_card_value(card):
    return int(card.split(',')[0])

