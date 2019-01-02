import random

print('Guess the number')

print(' : Rules')

print(" : Guess a number between 1 through 100")

print(' : If you guess it within 4 tries you win')

print ('------------------------------------------------ ')
max_guesses = 5

guesses = 1

numbers = random.randint(0, 100)
guess = -1
while guess != numbers:
    if guesses > max_guesses:
        print('you lose try again...\nnumber to guess been reset')
        numbers = random.randint(0, 100)
        guesses = 1
        continue

    guess_text = input('Guess a number 0 to 100:')
    guess = int(guess_text)

    if guess < numbers:
        print('to low')
    elif guess > numbers:
        print("to high")
    else:
        print('winner winner chicken dinner!!!!')

    guesses = guesses + 1



