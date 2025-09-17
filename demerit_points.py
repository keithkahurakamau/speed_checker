"""
This module contains the function to calculate demerit points based on vehicle speed.
It implements the logic for speed limit checking as per traffic rules.
"""

def calculate_demerit_points(speed):
    """
    Calculate the demerit points or status based on the given speed.

    Args:
        speed (float): The speed of the vehicle in km/h.

    Returns:
        str: "Ok" if speed is below limit, "Points: X" if within limit, or "License suspended" if over 12 points.
    """
    # Define the speed limit constant
    speed_limit = 70

    # Check if the speed is below the limit
    if speed < speed_limit:
        # If below limit, return "Ok" indicating no violation
        return "Ok"
    else:
        # Calculate demerit points: for every 5 km/h above limit, add 1 point
        # Use integer division to get whole points
        points = (speed - speed_limit) // 5

        # Check if points exceed the suspension threshold
        if points > 12:
            # If more than 12 points, license is suspended
            return "License suspended"
        else:
            # Otherwise, return the number of points as a string
            return f"Points: {int(points)}"
