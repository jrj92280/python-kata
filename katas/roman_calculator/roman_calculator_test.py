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
- If a lesser numeral is put before a bigger it means subtraction of the lesser from the bigger 
      (“IV” means four, “CM” means ninehundred)
- If the numeral is I, X or C you can’t have more than three (“II” + “II” = “IV”)
- If the numeral is V, L or D you can’t have more than one (“D” + “D” = “M”)
"""

from katas.roman_calculator.roman_calculator import roman_calculator


def test_numerals():
    test_cases = [
        ("", 0),
        ("I", 1),
        ("II", 2),
        ("III", 3),
        ("V", 5),
        ("VI", 6),
        ("X", 10),
        ("L", 50),
        ("C", 100),
        ("D", 500),
        ("M", 1000),
        ("XVI", 16),
    ]

    for roman_numeral_list, expected_value in test_cases:
        assert expected_value == roman_calculator(roman_numeral_list)


def test_subtraction():
    test_cases = [
        ("IV", 4), ("IM", 999), ("IMX", 1009)
    ]

    for roman_numeral_list, expected_value in test_cases:
        assert expected_value == roman_calculator(roman_numeral_list)
