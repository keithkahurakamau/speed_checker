from demerit_points import calculate_demerit_points

def check_speed():
    #get speed from user
    speed = float(input("Enter your speed in km/h: "))

    return calculate_demerit_points(speed)
    
    
def main():
    result = check_speed()
    print(result)
    
main()