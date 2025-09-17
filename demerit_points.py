def calculate_demerit_points(speed):
    speed_limit = 70
    if speed < speed_limit:
        return "Ok"
    else:
        points = (speed - speed_limit) // 5
        if points > 12:
            return "License suspended"
        else:
            return f"Points: {int(points)}"
