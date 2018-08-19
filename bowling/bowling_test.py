from bowling.bowling import score_game


def test_score_0():
    turns = frames()

    score = score_game(turns)
    assert score == 0


def frames():
    ten_frames = ["--" for _ in range(10)]
    turns = " ".join(ten_frames)
    return turns


def test_score_1():
    turns = frames()
    turns = "1" + turns[1:]
    score = score_game(turns)

    assert score == 1


def test_score_n():
    turns = frames()
    turns = "17" + turns[2:]
    score = score_game(turns)

    assert score == 8

print(("-- ".join(["" for _ in range(11)])).strip())
