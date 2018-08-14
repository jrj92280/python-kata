class Bowling:
    def __init__(self, rolls):
        self.rolls = rolls
        self.score = 0

    def calculate_score(self):
        if '1' in self.rolls:
            self.score = 1
