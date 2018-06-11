from chess_game.board import make_board


def test_make_board():
    board = make_board()
    assert 8 == len(board)
    for row in board:
        assert 8 == len(row)


def test_game_board_has_pawns():
    pawn_row = ["P" for _ in range(0, 8)]

    board = make_board()

    assert pawn_row == board[1]
    assert pawn_row == board[6]
