import pytest

from bowling.bowling import score_game


import pytest

from bowling.bowling import score_game


def test_score_0():
    turns = frames()

    score = score_game(turns)
    assert score == 0

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


def test_score_spare():
    turns = frames()
    turns = "1/" + turns[2:]
    score = score_game(turns)

    assert score == 10


def test_score_spare_1():
    turns = frames()
    turns = "1/ 1" + turns[4:]
    score = score_game(turns)

    assert score == 12


def test_score_spare_x():
    turns = frames()
    turns = "1/ X" + turns[4:]
    score = score_game(turns)

    assert score == 30

def test_score_bad_frames():
    bad_scenarios = []

    turns = frames()

    bad_scenarios.append(turns + '-')  # three rolls
    bad_scenarios.append('7')  # one roll one frame
    bad_scenarios.append(turns[3:])  # 9 frames
    bad_scenarios.append(turns[:-2] + "X X X X")
    bad_scenarios.append(turns[:-2] + "X X 9-")
    bad_scenarios.append(turns[:-2] + "X 9/ X")
    bad_scenarios.append("-X" + turns[2:])
    bad_scenarios.append("/1" + turns[2:])
    bad_scenarios.append("a1" + turns[2:])
    bad_scenarios.append("1a" + turns[2:])

    for bad_scenario in bad_scenarios:
        with pytest.raises(AssertionError):
            score_game(bad_scenario)

def test_score_boundary_frames():
    good_scenarios = []

    turns = frames()
    good_scenarios.append(turns[:-2] + "X --")
    good_scenarios.append(turns[:-2] + "X X -")
    good_scenarios.append(turns[:-2] + "X X X")
    good_scenarios.append(turns[:-2] + "X 8/")
    good_scenarios.append(turns[:-2] + "8/ X")

    for good_scenario in good_scenarios:
        score_game(good_scenario)

def frames():
    ten_frames = ["--" for _ in range(10)]
    turns = " ".join(ten_frames)
    return turns