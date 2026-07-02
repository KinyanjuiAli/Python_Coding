"""
Collatz Sequence Generator
Author: Hussein Kinyanjui
Book: Automate the Boring Stuff with Python - Chapter 3 Practice Project

This script takes an integer input from the user and executes the Collatz 
sequence logic until the resulting value reaches 1. It includes robust 
input validation to prevent crashes from non-integer inputs.
"""


def collatz(number: int) -> int:
    """
    Calculate the next number in the Collatz sequence.

    Args:
        number (int): The current integer in the sequence.

    Returns:
        int: The resulting integer after applying the Collatz rules.
    """
    # Check if the number is even
    if number % 2 == 0:
        result = number // 2
        print(result)
        return result

    # Otherwise, the number must be odd
    else:
        result = 3 * number + 1
        print(result)
        return result


def main():
    """Handle user input validation and execution of the sequence loop."""
    try:
        # Prompt user and convert input string to an integer
        user_input = int(input("Enter an integer: "))

        current_value = user_input

        # Continuously call collatz until the sequence safely hits 1
        while current_value != 1:
            current_value = collatz(current_value)

    except ValueError:
        # Gracefully handle non-integer string inputs like 'puppy'
        print("Error: You must enter an integer.")


# Standard Python boilerplate to ensure script runs when executed directly
if __name__ == "__main__":
    main()
