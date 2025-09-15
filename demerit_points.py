def calculate_demerit_points(speed):
    speed_limit = 70
    points_per_km = 5
    if (speed <=speed_limit):
     print("Ok")

    else:
       #calculate the demerit points
       demerit_points = (speed - speed_limit) // points_per_km