from chess_game_practice.chess_game import ChessGame
from chess_game_practice.commands.move_command import MoveCommand


def test_create_move_command():
    command = "1234"
    chess_game = ChessGame(None, None, None)

    move_command = MoveCommand(chess_game, command)
    assert command == move_command.command
    assert chess_game == move_command.chess_game


def test_parse_command_valid():
    command = "1234"
    move_command = MoveCommand(None, command)

    expected_command = ('move', ((1, 2), (3, 4)))

    assert expected_command == move_command.parse()
