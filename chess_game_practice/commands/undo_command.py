class UndoCommand:
    def __init__(self, chess_game, command):
        self.chess_game = chess_game
        self.command = command
        self.name = 'undo'

    def parse(self):
        if self.command != self.name:
            return False
        # current_position = (int(self.command[0]), int(self.command[1]))
        # target_position = (int(self.command[2]), int(self.command[3]))
        #
        # return_value = (self.name, (current_position, target_position))
        # return return_value
        pass
