class UndoCommand:
    def __init__(self, chess_game, command):
        self.chess_game = chess_game
        self.command = command
        self.name = 'undo'

    def parse(self):
        if self.command != self.name:
            return False

        self.chess_game.current_move_number = self.chess_game.current_move_number - 1
        self.chess_game.board = self.chess_game.moves[self.chess_game.current_move_number - 1]
        return True
