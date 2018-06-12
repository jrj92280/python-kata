from chess_game.board import make_board
from chess_game.chess_game import ChessGame

if __name__ == "__main__":
    game_board = make_board()

    print('play chess')
    print(' : Rules')
    print(' : Enter a move')
    print('------------------------------------------------')

    chess_game = ChessGame(game_board)

    game_event_loop()


def game_event_loop(chess_game):
    while true:
        print(chess_game)

        game_text = '\n\nMake A Move: '
        guess = get_user_input(game_text)


def get_user_input(text):
    user_move = input(text)

    return user_move
