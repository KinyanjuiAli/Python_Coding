"""
Comma Code
Author: Hussein Ali
Source: Automate the Boring Stuff with Python – Chapter 4: Lists

Description:
    Defines a function that accepts a list and returns a grammatically
    formatted string with items separated by commas and 'and' inserted
    before the final item — matching standard English list formatting.

Concepts Practised:
    - List slicing with [:-1] to exclude the last element
    - Negative indexing with [-1] to access the last element
    - String concatenation inside a for loop
    - Edge case handling with if statements for empty and single-item lists
"""


def comma_code(some_list: list) -> str:
    """
    Build a comma-separated string with 'and' before the final item.

    Args:
        some_list (list): A list of string items to be formatted.

    Returns:
        str: A formatted string e.g. 'apples, bananas, tofu, and cats'.
             Returns '' for an empty list.
             Returns the single item directly for a one-element list.
    """
    # An empty list has nothing to format — return early before any loop runs
    if len(some_list) == 0:
        return ''

    # A single item needs no comma or 'and' — return it directly
    if len(some_list) == 1:
        return some_list[0]

    result = ''

    # Slice excludes the last item so it can receive special 'and' formatting
    for item in some_list[:-1]:
        result = result + item + ', '

    # Append 'and' before the final item to complete standard English formatting
    result = result + 'and ' + some_list[-1]
    return result


if __name__ == "__main__":
    # Multiple items — expected: 'apples, bananas, tofu, and cats'
    print(comma_code(['apples', 'bananas', 'tofu', 'cats']))

    # Single item — expected: 'apples'
    print(comma_code(['apples']))

    # Empty list — expected: ''
    print(comma_code([]))
