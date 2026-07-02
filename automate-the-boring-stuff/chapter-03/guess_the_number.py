"""
Guess the Number Game
Author: [Your chosen full name]
Source: Automate the Boring Stuff with Python – Chapter 3: Functions

Description:
    A number-guessing game where the player attempts to identify a randomly
    generated integer between 1 and 20 within six attempts. Provides directional
    hints after each incorrect guess.

Concepts Practised:
    - Random number generation with the random module
    - for loops with range()
    - if/elif/else conditional logic
    - Input validation with try/except
    - Wrapping logic in a main() function with __name__ guard
"""

import random


def play_game() -> None:
    """
    Execute one full round of the guessing game.

    Generates a secret number, loops for up to 6 guesses, and prints
    the result. Input validation prevents non-integer entries from crashing
    the program.
    """
    secret_number = random.randint(1, 20)
    print("I am thinking of a number between 1 and 20.")

    for guesses_taken in range(1, 7):
        print("Take a guess.")

        try:
            guess = int(input())
        except ValueError:
            # Non-integer input should not crash the game — consume the turn instead
            print("Please enter a whole number.")
            continue

        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            # Correct guess — exit loop early
            break

    if guess == secret_number:
        print(f"Good job! You guessed my number in {guesses_taken} guesses!")
    else:
        print(f"Nope. The number I was thinking of was {secret_number}.")


def main() -> None:
    """Entry point — can be extended later to support replay logic."""
    play_game()


if __name__ == "__main__":
    main()
