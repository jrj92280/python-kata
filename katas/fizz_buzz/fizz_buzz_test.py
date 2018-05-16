from katas.fizz_buzz.fizz_buzz import fizz_buzz

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


def test_zero():
    assert [] == fizz_buzz(0)


def test_one():
    assert ['1'] == fizz_buzz(1)


def test_many():
    assert ['1', '2'] == fizz_buzz(2)


def test_fizz():
    assert ['1', '2', 'Fizz'] == fizz_buzz(3)


def test_buzz():
    assert ['1', '2', 'Fizz', '4', 'Buzz'] == fizz_buzz(5)


def test_fizz_buzz():
    assert ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14',
            'FizzBuzz'] == fizz_buzz(15)


def test_twenty():
    assert ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14',
            'FizzBuzz', '16', '17', 'Fizz', '19', 'Buzz'] == fizz_buzz(20)
