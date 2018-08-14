class Bowling:
    def __init__(self, rolls):
        self.rolls = rolls
        self.score = 0

    def calculate_score(self):
        frames = self.rolls.split(' ')

        for frame in frames:
            try:
                self.score += int(frame[0])
            except Exception:
                pass
            try:
                self.score += int(frame[1])
            except Exception:
                pass
