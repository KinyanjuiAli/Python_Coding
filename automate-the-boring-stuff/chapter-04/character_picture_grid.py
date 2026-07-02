"""
Character Picture Grid
Author: Hussein Ali
Source: Automate the Boring Stuff with Python – Chapter 4: Lists

Description:
    Stores a 2D image as a list of lists (a grid of characters), then prints
    it by transposing the grid — iterating over columns of the original data
    as rows of the printed output. This effectively rotates the image 90 degrees.

Concepts Practised:
    - Nested lists: a list whose elements are themselves lists
    - Nested for loops to traverse a 2D structure
    - Index-based access: grid[row][col]
    - Transposition: reading columns as rows to rotate printed output
    - end='' in print() to suppress automatic newlines
"""


def print_grid(grid: list) -> None:
    """
    Print a 2D character grid transposed by 90 degrees.

    Treats each inner list as a column of the image. The outer loop iterates
    over column positions and the inner loop iterates over rows — so each
    printed line corresponds to one column of the source data.

    Args:
        grid (list): A list of lists where each inner list represents one
                     vertical column of the character image.

    Returns:
        None
    """
    # Outer loop: step through each column position of the original grid
    # len(grid[0]) gives the number of elements in one inner list (the column depth)
    for col in range(len(grid[0])):

        # Inner loop: for the current column position, visit every row
        # len(grid) gives the total number of inner lists (rows in source data)
        for row in range(len(grid)):
            # end='' keeps all characters on the same printed line
            print(grid[row][col], end='')

        # After finishing one full column pass, move output to the next line
        print()


def main() -> None:
    """Define the character grid and print it transposed."""
    grid = [
        ['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']
    ]
    print_grid(grid)


if __name__ == "__main__":
    main()
