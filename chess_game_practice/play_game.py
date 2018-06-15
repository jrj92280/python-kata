from chess_game_practice.board import make_board
from chess_game_practice.chess_game import ChessGame


def game_event_loop(chess_game):
    while True:
        print(chess_game)

        game_text = '\n\nMake A Move (x,y,x2,y2): '
        move = get_user_input(game_text)
        current_position = [int(move[0]), int(move[1])]
        target_position = [int(move[2]), int(move[3])]
        chess_game.move_piece(current_position, target_position)


def get_user_input(text):
    while True:
        user_move = input(text)
        user_move = user_move.split(",")
        if len(user_move) != 4:
            print('invalid move')
            continue
        try:
            for move in user_move:
                if int(move) < 0 or int(move) > 7:
                    raise Exception()
        except:
            print("can't move there")
            continue

        return user_move


if __name__ == "__main__":
    game_board = make_board()

    print('play chess')
    print(' : Rules')
    print(' : Enter a move')
    print('------------------------------------------------')

    chess_game = ChessGame(game_board)

    game_event_loop(chess_game)
