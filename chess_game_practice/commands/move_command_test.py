from chess_game_practice.commands.move_command import MoveCommand


def test_create_move_command():
    command = "1234"
    move_command = MoveCommand(command)
    assert command == move_command.command


def test_parse_command_valid():
    command = "1234"
    move_command = MoveCommand(command)

    expected_command = ('move', ((1, 2), (3, 4)))

    assert expected_command == move_command.parse()
