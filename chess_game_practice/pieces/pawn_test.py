from chess_game_practice.board import make_board, _make_board_empty
from chess_game_practice.pieces.pawn import Pawn


def test_create_pawn():
    game_board = make_board()
    pawn = Pawn('x', 'y', "b", game_board)
    assert "pawn" == pawn.piece_type
    assert game_board == pawn.board
    assert "b" == pawn.color
    assert 'x' == pawn.x
    assert 'y' == pawn.y


def test_cant_move_on_self():
    game_board = _make_board_empty()
    game_board[6][0] = "bp"
    pawn = Pawn(0, 6, "b", game_board)
    assert False == pawn.move(0, 6)
