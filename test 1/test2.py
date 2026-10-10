calculate = input("What do you want to calculate? (speed,distance,time): \n").lower()

match calculate:
    case "speed":

        while True:
            try:
                distance = float(input("Enter distance: "))
                if distance <= 0:
                    raise Exception("Negatives or 0 cant be accepted! ")

                break
            except ValueError:
                print("Invalid input!")
            except Exception as e:
                print(f"Caught an error: {e}" )

        while True:
            try:
                time = float(input("Enter time: "))
                if time <= 0:
                    raise Exception("Negatives or 0 cant be accepted! ")

                break
            except ValueError:
                print("Invalid input!")
            except Exception as e:
                print(f"Caught an error: {e}" )

        print(f"Speed = {distance/time}")
