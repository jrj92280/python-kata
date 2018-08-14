from bowling.bowling import Bowling


def test_zero():
    # arrange
    rolls = '-- -- -- -- -- -- -- -- -- --'
    bowling = Bowling(rolls)

    # act
    bowling.calculate_score()

    # assert
    assert 0 == bowling.score


def test_one():
    # arrange
    rolls = '1- -- -- -- -- -- -- -- -- --'
    bowling = Bowling(rolls)

    # act
    bowling.calculate_score()

    # assert
    assert 1 == bowling.score


def test_two():
    # arrange
    rolls = '1- -- -- -- -- -- -- -- 1- --'
    bowling = Bowling(rolls)

    # act
    bowling.calculate_score()

    # assert
    assert 2 == bowling.score


def test_three():
    # arrange
    rolls = '1- -- -- -- -- -5 1- -- -- --'
    bowling = Bowling(rolls)

    # act
    bowling.calculate_score()

    # assert
    assert 7 == bowling.score
