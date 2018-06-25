from chess_game_practice.board import make_board


def test_make_board():
    board = make_board()
    assert 8 == len(board)
    for row in board:
        assert 8 == len(row)


def test_game_board_has_pawns():
    black_pawn_row = ["BP" for _ in range(0, 8)]
    white_pawn_row = ["WP" for _ in range(0, 8)]
    board = make_board()

    assert white_pawn_row == board[1]
    assert black_pawn_row == board[6]


def test_game_board_has_empty_spaces():
    empty_row = ["##" for _ in range(0, 8)]

    board = make_board()

    assert empty_row == board[2]
    assert empty_row == board[3]
    assert empty_row == board[4]
    assert empty_row == board[5]


def test_game_board_has_white_pieces():
    white_pieces = ["WR", "WH", "WB", "WK", "WQ", "WB", "WH", "WR"]

    board = make_board()

    assert white_pieces == board[0]


def test_game_board_has_black_pieces():
    black_pieces = ["BR", "BH", "BB", "BQ", "BK", "BB", "BH", "BR"]

    board = make_board()

    assert black_pieces == board[7]
