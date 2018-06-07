def roman_calculator(roman_numeral_list):
    total = 0

    subtraction_value = 0

    for position, numeral in enumerate(roman_numeral_list):
        current_numeral_value = get_numeral_value(numeral)

        if subtraction_value:
            current_numeral_value = current_numeral_value - subtraction_value
            subtraction_value = 0

        next_position = position + 1
        list_length = len(roman_numeral_list)

        if next_position < list_length:
            next_numeral = roman_numeral_list[next_position]
            next_numeral_value = get_numeral_value(next_numeral)

            if next_numeral_value > current_numeral_value:
                subtraction_value = current_numeral_value
                continue

        total = total + current_numeral_value

    return total


def get_numeral_value(numeral):
    numeral_values = {
        "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
    }

    numeral_value = numeral_values.get(numeral, 0)

    return numeral_value


if __name__ == '__main__':
    print(roman_calculator('IV'))
