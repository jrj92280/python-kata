def score_game(turns: str) -> int:
    frames = turns.split(' ')
    assert len(frames) == 10

    score = 0
    is_spare = False

    for frame in frames:
        assert len(frame) == 2 or len(frame) == 1

        if len(frame) == 1:
            continue

        turn_1 = frame[0]
        turn_2 = frame[1]

        if is_spare:
            score = score_turn(score, turn_1)
            is_spare = False

        if turn_2 == '/':
            score += 10
            is_spare = True
            continue

        score = score_turn(score, turn_1)
        score = score_turn(score, turn_2)

    return score


def score_turn(score, turn):
    try:
        score += int(turn)
    except:
        if turn == 'X':
            score += 10

    return score
