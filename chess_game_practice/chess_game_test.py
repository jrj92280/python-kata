from chess_game_practice.board import make_board
from chess_game_practice.chess_game import ChessGame


def test_create_chess_game():
    # calling the fuction make board and assign to board
    board = make_board()
    player_one = 'player_one'
    player_two = 'player_two'
    # create new instance of ChessGame
    chess_game = ChessGame(board, player_one, player_two)

    assert board == chess_game.board
    assert player_one == chess_game.player_one
    assert player_two == chess_game.player_two

    assert chess_game.board is not chess_game.moves[0]
    assert chess_game.board == chess_game.moves[0]


def test_move_piece():
    board = make_board()
    chess_game = ChessGame(board, None, None)

    chess_game.move_piece([0, 1], [0, 3])

    assert "##" == chess_game.board[1][0]
    assert "WP" == chess_game.board[3][0]
