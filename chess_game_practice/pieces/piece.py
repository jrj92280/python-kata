class Piece:
    def __init__(self, x, y, color, piece_type, board):
        self.board = board
        self.x = x
        self.y = y
        self.color = color
        self.piece_type = piece_type
        self.has_moved = False

    def move(self, x, y):
        self.has_moved = True
        return self._move(x, y)

    def _move(self):
        raise NotImplemented
