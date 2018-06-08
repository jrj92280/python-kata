import random

print('Guess the number')
print(' : Rules')
print(" : Guess a number between 1 through 100")
print(' : If you guess it within 5 tries you win')
print('------------------------------------------------')

tracking_list = []
max_guesses = 5
guesses = 1
numbers = random.randint(0, 100)
guess = -1

top_int = 100
lower_int = 0

def game_event_loop():
    global numbers, guesses, guess, top_int, lower_int
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
                           'Guess a number ' + str(lower_int) + ' to ' + str(top_int) + ': ')
        tracking_list.append(guess_text)

        guess = int(guess_text)

        if guess < numbers:
            print('to low')
            lower_int = guess
        elif guess > numbers:
            print("to high")
            top_int = guess

        else:
            print('winner winner chiken dinner!!!!')

        guesses = guesses + 1


game_event_loop()
