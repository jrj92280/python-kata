def fizz_buzz(upper_bound):
    numbers = []

    for number in range(1, upper_bound + 1):
        if number % 3 == 0 and number % 5 == 0:
            numbers.append('FizzBuzz')
        elif number % 3 == 0:
            numbers.append('Fizz')
        elif number % 5 == 0:
            numbers.append('Buzz')
        else:
            numbers.append(str(number))

    return numbers


if __name__ == '__main__':
    print(fizz_buzz(100))
