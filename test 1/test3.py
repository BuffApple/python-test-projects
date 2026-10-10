calculate = input("What do you want to calculate?(speed,distance,time): ").lower()

def calculate_distance():
    dist = 0
    while True:
        try:
            dist = float(input("Enter distance: "))
        except ValueError:
            print("Please enter a valid number!")
            continue
        if dist <=0 :
            print("Distance cant be 0/negative!")
            continue
        break
    return dist


def calculate_time():
    ti = 0
    while True:
        try:
            ti = float(input("Enter Time: "))
        except ValueError:
            print("Please enter a valid number!")
            continue
        if ti <= 0:
            print("Time cant be 0/negative!")
            continue
        break
    return ti


match calculate:
    case "speed":
        distance = calculate_distance()
        time = calculate_time()
        print(f"Speed = {distance/time}")



