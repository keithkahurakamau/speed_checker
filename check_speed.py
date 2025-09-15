def check_speed():
    #get speed from user
    speed = float(input("Enter your speed in km/h: "))
    
    #check if speed is within limit
    if speed < 70:
        return "Ok"
    else:
        points = (speed - 70) // 5
        if points > 12:
            return "License suspended"
        else:
            return f"Points: {int(points)}"
    
    
def main():
    result = check_speed()
    print(result)
    
main()