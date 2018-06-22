from chess_game_practice.commands.move_command import MoveCommand


def test_create_move_command():
    command = "1234"
    move_command = MoveCommand(command)
    assert command == move_command.command
