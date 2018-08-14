from bowling.bowling import Bowling


def test_zero():
    rolls = '-- -- -- -- -- -- -- -- -- --'
    bowling = Bowling(rolls)
    bowling.calculate_score()
