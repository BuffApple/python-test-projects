
calculate = input("What do you want to calculate? (speed,distance,time): ")

calculate = calculate.lower()

match calculate:
    case "speed":
        distance = input("Enter distance: ")
        while not distance.isdigit() or not int(distance):
            distance = input("Please enter a valid number: ")
        distance = int(distance)

        time = input("Enter time: ")
        while not time.isdigit() or not int(time):
            time = input("Please enter a valid number: ")
        time = int(time)

        print(f"Speed = {distance/time}")

    case "distance":
        speed = input("Enter speed: ")
        while not speed.isdigit() or not int(speed) :
            speed = input("Please enter a valid number: ")
        speed = int(speed)

        time = input("Enter time: ")
        while not time.isdigit() or not int(time):
            time = input("Please enter a valid number: ")
        time = int(time)

        print(f"Distance = {speed*time}")

    case "time":
        speed = input("Enter speed: ")
        while not speed.isdigit() or not int(speed):
            speed = input("Please enter a valid number: ")
        speed = int(speed)

        distance = input("Enter distance: ")
        while not distance.isdigit() or not int(distance):
            distance = input("Please enter a valid number: ")
        distance = int(distance)

        print(f"Time = {distance/speed}")

    case _:
        print("Enter something valid next time you little shit")