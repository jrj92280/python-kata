def opperation(x, y, op):
    if op == '+':
        return x + y
    if op == '-':
        return x - y
    if op == '/':
        return x / y
    if op == '*':
        return x * y


assert 8 == opperation(3, 5, '+')

assert -2 == opperation(3, 5, '-')

assert 2 == opperation(6, 3, '/')

assert 18 == opperation(6, 3, '*')

x = opperation(10, 8, '+')

# write a method called calculator that takes a string argument and returns the calculated result
# "1 + 3" => 4
# "3 - 5" => -2
# "3 + 4 - 5" => 2

calculation = "2 + 5 * 2"


def calculator(value):
    split_value = value.split(' ')

    has_multiplication = True
    offset = 1

    while len(split_value) != 1:
        if len(split_value) <= offset:
            offset = 1
            has_multiplication = False
            continue

        if has_multiplication and \
                (split_value[offset] == '+' or split_value[offset] == '-'):
            offset += 2
            continue
        result = opperation(int(split_value[offset - 1]), int(split_value[offset + 1]), split_value[offset])

        split_value.pop(offset - 1)
        split_value.pop(offset - 1)
        split_value.pop(offset - 1)
        split_value.insert(offset - 1, result)
        offset = 1

    return split_value[0]


# write here


print(calculator(calculation))

assert 4 == calculator("1 + 3")
assert 6 == calculator("1 + 3 + 2")
assert 10 == calculator('1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1')
assert 12 == calculator('2 + 5 * 2')
assert 5 == calculator('2 + 6 / 2')
assert 18 == calculator('2 + 5 * 2 + 2 * 3')
assert 30 == calculator('2 + 5 * 2 * 3 - 2')
