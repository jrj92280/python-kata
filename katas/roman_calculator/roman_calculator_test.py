"""
Z - Zero x
O - One x
M - Many x
B - Boundary Behaviors
I - Interface Definition x
E - Exercise Exceptional x
S - Simple Scenarios, Simple Solutions
"""

"""
TDD : Test Driven Development

1. You are not allowed to write any production code unless it is to make a failing unit test pass.
2. You are not allowed to write any more of a unit test than is sufficient to fail; and compilation failures are failures.
3. You are not allowed to write any more production code than is sufficient to pass the one failing unit test.
"""

"""
**There are some rules to a Roman number:**
- Numerals can be concatenated to form a larger numeral (“XX” + “II” = “XXII”)
- If a lesser numeral is put before a bigger it means subtraction of the lesser from the bigger (“IV” means four, “CM” means ninehundred)
- If the numeral is I, X or C you can’t have more than three (“II” + “II” = “IV”)
- If the numeral is V, L or D you can’t have more than one (“D” + “D” = “M”)
"""

from katas.roman_calculator.roman_calculator import roman_calculator


def test_zero():
    assert 0 == roman_calculator("")


def test_one():
    assert 1 == roman_calculator("I")


def test_two():
    assert 2 == roman_calculator("II")


def test_three():
    assert 3 == roman_calculator("III")


def test_five():
    assert 5 == roman_calculator("V")


def test_six():
    assert 6 == roman_calculator("VI")


def test_ten():
    assert 10 == roman_calculator("X")
