class card:
    def __init__(self, cards):
        self.cards = cards
        self.card = self.cards

    def __repr__(self):
        return self.cards


class poker_hand():
    def __init__(self, card_list):
        self.card_list = card_list
