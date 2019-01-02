from random import shuffle
class Gun:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.chambers = [None for _ in range(capacity)]

    def load(self, bullet: str):
        for index, chamber in enumerate(self.chambers):
            if not chamber:
                self.chambers[index] = bullet
                break

    def shuffle(self):
        shuffle(self.chambers)


class Player:
    def __init__(self):
        self.alive = True

    def take_turn(self, gun: Gun) -> Gun:
        pass


if __name__ == '__main__':
    player = Player()

    gun = Gun(6)
    gun.load("bullet")
    gun.shuffle()
    print(gun.chambers)
    gun.shuffle()
    print(gun.chambers)
