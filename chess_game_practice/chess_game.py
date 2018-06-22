class ChessGame:
    def __init__(self, board, player_one, player_two):
        self.board = board
        self.player_one = player_one
        self.player_two = player_two

    def __str__(self):
        return "\n".join([str(row) for row in self.board])

    def move_piece(self, current_position, target_position):
        cy = current_position[1]
        cx = current_position[0]
        piece = self.board[cy][cx]

        ty = target_position[1]
        tx = target_position[0]

        self.board[ty][tx] = piece
        self.board[cy][cx] = '##'
