class MoveCommand:
    def __init__(self, command):
        self.command = command

    def parse(self):
        command = self.command.split(",")
        if len(command) != 4:
            print('invalid move')
            return False
        try:
            for move in command:
                if int(move) < 0 or int(move) > 7:
                    raise Exception()
        except:
            print("can't move there")
            return False
