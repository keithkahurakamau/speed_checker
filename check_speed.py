"""
This module provides a command-line interface for checking vehicle speed against traffic limits.
It prompts the user for speed input and displays the result based on demerit point calculations.
"""

from demerit_points import calculate_demerit_points

def check_speed():
    """
    Prompt the user for speed input and determine the speed check result.

    Returns:
        str: The result of the speed check ("Ok", "Points: X", or "License suspended").
    """
    # Prompt the user to enter the vehicle speed in km/h
    speed = float(input("Enter your speed in km/h: "))

    # Call the demerit points calculation function with the input speed
    return calculate_demerit_points(speed)


def main():
    """
    Main function to run the speed checker program.
    Gets the result from check_speed and prints it to the console.
    """
    # Get the speed check result
    result = check_speed()
    # Print the result to the user
    print(result)


# Execute the main function when the script is run directly
main()
