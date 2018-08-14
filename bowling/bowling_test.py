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
