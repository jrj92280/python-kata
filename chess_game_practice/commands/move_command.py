class MoveCommand:
    def __init__(self, command):
        self.command = command
        self.name = 'move'

    def parse(self):
        current_position = (int(self.command[0]), int(self.command[1]))
        target_position = (int(self.command[2]), int(self.command[3]))

        return_value = (self.name, (current_position, target_position))
        return return_value
