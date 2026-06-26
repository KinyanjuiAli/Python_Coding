"""
Guess the Number Game
Author: Hussein Ali
Book: Automate the Boring Stuff with Python - Chapter 3 Practice Project

A classic number-guessing game where the player attempts to guess a randomly 
generated number between 1 and 20 within six attempts.
"""

import random

# Generate a random secret number between 1 and 20 inclusive
secret_number = random.randint(1, 20)

print("I am thinking of a number between 1 and 20.")

# Give the player exactly 6 opportunities to guess
for guesses_taken in range(1, 7):
    print("Take a guess.")
    guess = int(input())

    # Provide hints based on the player's guess
    if guess < secret_number:
        print("Your guess is too low.")
    elif guess > secret_number:
        print("Your guess is too high.")
    else:
        # The guess matches the secret number, break out of the loop early
        break

# Check the final result after the loop finishes
if guess == secret_number:
    print(
        f"Good job! You guessed my number in {guesses_taken} guesses!"
    )
else:
    print(f"Nope. The number I was thinking of was {secret_number}")
