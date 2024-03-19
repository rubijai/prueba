'''Adivinar un numero entre 1 y 100'''
import random as rn

dificultad = input('Dificil, escriba d. Facil, escriba f: ')
if dificultad == 'd':
    chances = 5
elif dificultad == 'f':
    chances = 10
else:
    print('no uso d o f')
num_adiv = rn.randint(1, 100)
while chances != 0:
    guess = int(input('entre posible numero : '))
    if guess == num_adiv:
        print(f'Ud adivino, el numero es {guess}')
    elif guess > num_adiv:
        print('muy alto')
    else:
        print('muy bajo')
    chances -= 1
    if chances == 0:
        print(f'El numero es {num_adiv}')

from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


# Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
    """checks answer against guess. Returns the number of turns remaining."""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")


# Make function to set difficulty.
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    # Choosing a random number between 1 and 100.
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")

    turns = set_difficulty()
    # Repeat the guessing functionality if they get it wrong.
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

        # Let the user guess a number.
        guess = int(input("Make a guess: "))

        # Track the number of turns and reduce by 1 if they get it wrong.
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")


game()
