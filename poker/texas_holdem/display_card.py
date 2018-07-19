def display_card(card):
    suit = card[0]
    card_value = card[1:]

    if suit == 'H':
        suit = '♥'

    if suit == 'C':
        suit = '♣'

    if suit == 'S':
        suit = '♠'

    if suit == 'D':
        suit = '♦'

    if card_value == '11':
        card_value = 'J'

    if card_value == '12':
        card_value = 'Q'

    if card_value == '13':
        card_value = 'K'

    if card_value == '14':
        card_value = 'A'


    return card_value + suit
