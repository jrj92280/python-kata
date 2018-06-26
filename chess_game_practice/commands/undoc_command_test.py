from chess_game_practice.chess_game import ChessGame
from chess_game_practice.commands.undo_command import UndoCommand


def test_create_undo_command():
    command = "undo"
    chess_game = ChessGame(None, None, None)

    undo_command = UndoCommand(chess_game, command)
    assert command == undo_command.command
    assert chess_game == undo_command.chess_game


# def test_parse_command_valid():
#     command = "undo"
#     undo_command = UndoCommand(None, command)
#
#     expected_command = ('undo', ())
#
#     assert expected_command == undo_command.parse()

def test_parse_not_undo():
    command = 'not_undo'
    undo_command = UndoCommand(None, command)

    expected_command = False
    assert expected_command == undo_command.parse()
