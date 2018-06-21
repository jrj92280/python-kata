import copy

from chess_game_practice.board import make_board
from chess_game_practice.chess_game import ChessGame


def game_event_loop(chess_game, player1_name, player2_name, player_moves):
    current_move_number = 1
    _moves = [copy.deepcopy(chess_game.board)]

    while True:
        print(chess_game)

        if current_move_number % 2 == 1:
            current_player_name = player1_name
        else:
            current_player_name = player2_name
        print('Player: ' + current_player_name)

        game_text = '\n\nMake A Move (x,y,x2,y2): '
        move = get_user_input(game_text)

        if move == 'undo':
            current_move_number = current_move_number - 1
            chess_game.board = _moves[current_move_number - 1]
            continue
        # calculate current and target postition
        current_position = [int(move[0]), int(move[1])]
        target_position = [int(move[2]), int(move[3])]

        # move the piece
        chess_game.move_piece(current_position, target_position)
        _moves.append(copy.deepcopy(chess_game.board))
        current_move_number = current_move_number + 1


def get_user_input(text):
    while True:
        user_move = input(text)

        if user_move == 'undo':
            return user_move

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

    print('Chess')
    print(' : Rules')
    print('   : input - piece''s position x,y, second x,y = destination')
    print("   : x = row number 1 though 8")
    print("   : y = column number 1 though 8")

    player1_name = input(' : Enter player one name')
    player2_name = input(' : Enter player two name')

    moves = {
        player1_name: list(),
        player2_name: list()
    }

    print('------------------------------------------------')

    chess_game = ChessGame(game_board)

    game_event_loop(chess_game, player1_name, player2_name, moves)
