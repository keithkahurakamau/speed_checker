def check_speed():
    #get speed from user
    speed = float(input("Enter your speed in km/h: "))
    
    #check if speed is within limit
    if speed <= 70:
        return "Ok"
    else:
        return "Over speed limit!!"
    
    
def main():
    result = check_speed()
    print(result)
    
main()