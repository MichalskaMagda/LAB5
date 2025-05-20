"""Module for converting numbers to binary representation."""


def convert_to_binary(number):
    """Converts an integer to its binary representation."""
    if not isinstance(number, int):
        raise TypeError("Input must be an integer.")
    if number < 0 or number > 100:
        raise ValueError("Number must be between 0 and 100.")
    return bin(number)[2:]  # Usuwa '0b' z przodu
