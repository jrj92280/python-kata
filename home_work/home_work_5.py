"""
https://adriann.github.io/programming_problems.html

Elementary
Write a program that prints ‘Hello World’ to the screen.
Write a program that asks the user for their name and greets them with their name.
Modify the previous program such that only the users Alice and Bob are greeted with their names.

Write a program that asks the user for a number n and prints the sum of the numbers 1 to n
Modify the previous program such that only multiples of three or five are considered in the sum, e.g. 3, 5, 6, 9, 10, 12, 15 for n=17
"""


def user():
    x = input('Enter your name: ')
    greeting = 'Hello'

    if x.lower() in ['alice', 'bob']:
        greeting += ' ' + x

    return greeting


# print(user())print ('How are you doing?')


def _print_numbers():
    x = input('Enter a number: ')
    x = int(x)
    return x * (x + 1) / 2


def print_numbers():
    x = input('Enter a number: ')
    x = int(x)

    total = 0

    for number in range(1, x + 1):
        if number % 3 == 0 or number % 5 == 0:
            total = total + number

    return total


print(print_numbers())
