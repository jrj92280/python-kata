# hair = input("What color hair[brown]?")
# if hair == '':
#     hair = 'brown'
# print('You chose', hair)
#
# hair_length = input("What hair length [short]?")
# if hair_length == '':
#     hair_length = 'short'
# print('You chose', hair_length)
#
# eyes = input("What eye color [blue]?")
# if eyes == '':
#     eyes = 'blue'
# print("You chose', eyes")
#
# gender = input("What gender [female]?")
# if gender == '':
#     gender = 'female'
# print('You chose gender', gender)
#
# has_glasses = input("Has glasses [no]?")
# if has_glasses == '':
#     has_glasses = 'no'
# print('You chose', has_glasses)
#
# has_beard = input("Has beard [no]?")
# if has_beard == '':
#     has_beard = 'no'
# print('You chose', has_beard)

# /// page 199//

def get_attribute(query, default):
    question = query + ' [' + default + ']? '
    answer = input(question)
    if (answer == ''):
        answer = default
    print('You chose)', answer)
    return answer


hair = get_attribute('What hair color', 'brown')
hair_length = get_attribute('What hair length', 'short')
eye = get_attribute('What eye color', 'blue')
gender = get_attribute('What gender', 'female')
glasses = get_attribute('Sas glasses', 'no')
beard = get_attribute('Has beard', 'no')
