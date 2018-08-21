def score_game(turns: str) -> int:
    frames = get_frames(turns)

    score = 0
    is_spare = False

    for frame_index, frame in enumerate(frames):
        assert len(frame) == 2 or len(frame) == 1

        if frame_index == 10 and len(frame) == 2:
            assert len(frames) == 11

        if frame_index == 11:
            assert len(frame) == 1

        if len(frame) == 1:
            continue

        turn_1 = frame[0]
        if turn_1 not in "-123456789X":
            assert False
        turn_2 = frame[1]

        if turn_2 not in "-123456789/":
            assert False

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


def get_frames(turns):
    frames = turns.split(' ')

    if len(frames) < 10:
        assert False
    if len(frames) > 12:
        assert False
    if frames[9] == "X" or "/" in frames[9]:
        pass
    else:
        assert len(frames) == 10
    return frames


def score_turn(score, turn):
    try:
        score += int(turn)
    except:
        if turn == 'X':
            score += 10

    return score
