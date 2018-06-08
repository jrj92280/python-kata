import random

print('Guess the number')

print(' : Rules')

print(" : Guess a number between 1 through 100")

print(' : If you guess it within 4 tries you win')

print('------------------------------------------------ ')

tracking_list = []
max_guesses = 5
guesses = 1
numbers = random.randint(0, 100)
guess = -1


def game_event_loop():
    global numbers, guesses, guess
    while guess != numbers:
        if guesses > max_guesses:
            # print my guesses and the actual value
            print('\n'
                  'player guesses: ' + str(tracking_list))
            print('game number was: ' + str(numbers))
            print('\n'
                  'you lose try again...\n\n'
                  'number to guess been reset')

            numbers = random.randint(0, 100)
            guesses = 1
            continue

        guess_text = input('\n'
                           'Guess a number 0 to 100: ')
        tracking_list.append(guess_text)

        guess = int(guess_text)

        if guess < numbers:
            print('to low')
        elif guess > numbers:
            print("to high")
        else:
            print('winner winner chiken dinner!!!!')

        guesses = guesses + 1


game_event_loop()
