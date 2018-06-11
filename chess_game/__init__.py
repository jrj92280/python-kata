from chess_game.board import make_board

if __name__ == "__main__":
    game_board = make_board()
    print("\n".join([str(row) for row in game_board]))
