def roman_calculator(roman_numeral):
    total = 0

    for numeral in roman_numeral:
        # todo: find numeral of character
        numeral_value = 1
        if numeral == 'V':
            numeral_value = 5
        elif numeral == 'X':
            numeral_value = 10

        total = total + numeral_value

    return total


if __name__ == '__main__':
    print(roman_calculator('IV'))
