class ChessGame:
    def __init__(self, board):
        self.board = board

    def __str__(self):
        return "\n".join([str(row) for row in self.board])

    def move_piece(self, current_position, target_position):
        cy = current_position[1]
        cx = current_position[0]
        piece = self.board[cy][cx]

        ty = target_position[1]
        tx = target_position[0]

        self.board[ty][tx] = piece
        self.board[cy][cx] = '#'
