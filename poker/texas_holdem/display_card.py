def display_card(card):
    suit = card[0]

    if suit == 'H':
        suit = '♥'

    card_value = card[1:]

    # if 11 card value = J

    return card_value + suit
