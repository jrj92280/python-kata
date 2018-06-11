def make_board():
    game_board = []

    for _ in range(0, 8):
        row = []
        for position in range(0, 8):
            row.append("O")
        game_board.append(row)

    print(game_board)
    return game_board
