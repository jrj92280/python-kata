def score_game(turns: str) -> int:
    frames = turns.split(' ')
    assert len(frames) == 10

    score = 0
    for frame in frames:
        assert len(frame) == 2 or len(frame) == 1

        if len(frame) == 1:
            continue

        turn_1 = frame[0]
        turn_2 = frame[1]

        try:
            score += int(turn_1)
        except:
            pass

        try:
            score += int(turn_2)
        except:
            pass

    return score
