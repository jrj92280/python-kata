from chess_game_practice.pieces.piece import Piece


class Pawn(Piece):
    def __init__(self, x, y, color, board):
        super().__init__(x, y, color, "pawn", board)

    def _move(self, x, y):
        if self.x == x and self.y == y:
            return False

        print(self.x + self.y)
