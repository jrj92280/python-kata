import copy

from chess_game_practice.board import make_board
from chess_game_practice.chess_game import ChessGame
from chess_game_practice.commands.move_command import MoveCommand
from chess_game_practice.commands.undo_command import UndoCommand
from chess_game_practice.pieces.pawn import Pawn


def game_event_loop(chess_game):
    _moves = chess_game.moves

    while True:
        print(chess_game)

        if chess_game.current_move_number % 2 == 1:
            current_player_name = chess_game.player_one
        else:
            current_player_name = chess_game.player_two
        print('Player: ' + current_player_name)

        game_text = '\n\nMake A Move (x,y,x2,y2): '
        move = get_user_input(game_text)

        undo_command = UndoCommand(chess_game, move)
        if undo_command.parse():
            continue

        move_command = MoveCommand(chess_game, move)
        command = move_command.parse()

        # calculate current and target postition
        current_position = command[1][0]
        target_position = command[1][1]

        # move the piece
        chess_game.move_piece(current_position, target_position)

        _moves.append(copy.deepcopy(chess_game.board))
        chess_game.current_move_number = chess_game.current_move_number + 1


def get_user_input(text, is_move=True):
    while True:
        user_input = input(text)

        # command = parse_command(user_input, is_move=is_move)
        # if not command:
        #     continue

        return user_input


def parse_command(command, is_move=True):
    if not command:
        return False

    if command == 'undo':
        return command

    if is_move:
        command = command.split(",")
        if len(command) != 4:
            print('invalid move')
            return False
        try:
            for move in command:
                if int(move) < 0 or int(move) > 7:
                    raise Exception()
        except:
            print("can't move there")
            return False

    return command






if __name__ == "__main__":
    game_board = make_board()
    pawn = Pawn('x', 'y', None, None, None)
    pawn.move()

    a_list = MyList(["a", "b"])
    a_list.append("x")
    print(a_list.pop())

    print('Chess')
    print(' : Rules')
    print('   : input - piece''s position x,y, second x,y = destination')
    print("   : x = row number 1 though 8")
    print("   : y = column number 1 though 8")

    player1_name = get_user_input(' : Enter player one name', is_move=False)
    player2_name = get_user_input(' : Enter player two name', is_move=False)

    print('------------------------------------------------')

    chess_game = ChessGame(game_board, player1_name, player2_name)

    game_event_loop(chess_game)
