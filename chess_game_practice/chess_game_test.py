from chess_game_practice.chess_game import ChessGame


def test_create_chess_game():
    # calling the fuction make board and assign to board
    board = make_board()
    # create new instance of ChessGame
    chess_game = ChessGame(board)

    assert board == chess_game.board


def test_move_piece():
    board = make_board()
    chess_game = ChessGame(board)

    chess_game.move_piece([0, 1], [0, 3])

    assert "#" == chess_game.board[1][0]
    assert "WP" == chess_game.board[3][0]
