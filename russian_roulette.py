class Gun:
    def __init__(self, capacity: int):
        self.capacity = capacity


class Player:
    def __init__(self):
        self.alive = True

    def take_turn(self, gun: Gun) -> Gun:
        pass


if __name__ == 'main':
    player = Player()
