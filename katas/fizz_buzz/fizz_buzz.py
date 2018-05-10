input = 100


def fizz_buzz(upperbound):
    for number in range(1, upperbound+1):
        if number % 3 == 0:
            print('fizz')
        elif number == 100:
            print('2222')
        else :
            print(number)

fizz_buzz(input)
