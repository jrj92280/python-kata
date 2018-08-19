from bowling.bowling import score_game


def test_score_0():
    score = score_game('')
    assert score == 0


print(("-- ".join(["" for _ in range(11)])).strip())
