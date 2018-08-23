min_frames = 10
max_frames = 12

vaild_turn_one_values = "-123456789X"
vaild_turn_two_values = "-123456789/"

turn_one_index = 0
turn_two_index = 1


def score_game(turns: str) -> int:
    frames = get_frames(turns)
    validate_frames(frames)

    score = 0
    previous_was_spare = False

    for frame_index, frame in enumerate(frames):
        score += score_frame(frame_index, frame, previous_was_spare)
        previous_was_spare = is_spare(frame)

    return score


def score_frame(frame_index: int, frame: str, previous_was_spare: bool) -> int:
    score = 0

    assert len(frame) == 2 or len(frame) == 1

    if frame_index == 11:
        assert len(frame) == 1

    if len(frame) == 1:
        return 0

    turn_1 = validate_turn(frame, turn_one_index, vaild_turn_one_values)
    turn_2 = validate_turn(frame, turn_two_index, vaild_turn_two_values)

    if previous_was_spare:
        score = score_turn(score, turn_1)

    if is_spare(turn_2):
        score += 10
    else:
        score = score_turn(score, turn_1)
        score = score_turn(score, turn_2)

    return score

def get_frames(turns):
    frames = turns.split(' ')
    return frames


def validate_frames(frames):
    frame_count = len(frames)

    tenth_frame = get_tenth_frame(frames)
    eleventh_frame = get_eleventh_frame(frames)

    if frame_count < min_frames or frame_count > max_frames:
        assert False

    if not is_strike(tenth_frame) and not is_spare(tenth_frame):
        assert frame_count == 10

    if is_spare(eleventh_frame):
        assert frame_count == 11



def get_tenth_frame(frames):
    return get_frame(frames, 9)


def get_eleventh_frame(frames):
    return get_frame(frames, 10)


def get_frame(frames, index):
    frame_count = len(frames)
    return frames[index] if frame_count > index else None


def is_spare(frame):
    return frame and '/' in frame


def is_strike(frame):
    return 'X' in frame


def has_twleve_frames(frames):
    return len(frames) == 12

def validate_turn(frame, turn_index, vaild_turn_one_values):
    turn_1 = frame[turn_index]
    if turn_1 not in vaild_turn_one_values:
        assert False
    return turn_1


def score_turn(score, turn):
    try:
        score += int(turn)
    except:
        if turn == 'X':
            score += 10

    return score