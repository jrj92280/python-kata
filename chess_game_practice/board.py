def make_board():
    game_board = []

    for row_index in range(0, 8):
        row = []

        for position in range(0, 8):
            if row_index == 1:
                row.append("WP")
            elif row_index == 6:
                row.append("BP")
            else:
                row.append("##")

        game_board.append(row)

    white_pieces = ["WR", "WH", "WB", "WK", "WQ", "WB", "WH", "WR"]
    game_board[0] = white_pieces

    black_pieces = ["BR", "BH", "BB", "BQ", "BK", "BB", "BH", "BR"]
    game_board[7] = black_pieces
    # print("\n".join([str(row) for row in game_board]))

    return game_board
