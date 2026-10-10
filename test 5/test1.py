def get_numeric_data(question):
    data = 0
    while True:
        try:
            data = float(input(question))
        except ValueError:
            print("Please enter a number!")
            continue
        if data < 0:
            print("You cant enter negative numbers!")
            continue
        return data

crew_size = 4
number_of_days = 0
oxygen_per_day = get_numeric_data("Please enter oxygen needed per day: ")
food_per_day = get_numeric_data("Please enter food needed per day: ")
maximum_oxygen = get_numeric_data("Please enter maximum oxygen that can be stored: ")
maximum_food = get_numeric_data("Please enter maximum food that can be stored: ")

artemisII = ["2","artemis ii","artemisii"]
artemisIII = ["3","artemis iii","artemisiii"]


while True:
    mission = input("Please choose a mission:(2.Artemis II, 3.Artemis III) ").lower()
    if mission in artemisII:
        mission = "Artemis II"
        number_of_days = 10
        break
    elif mission in artemisIII:
        mission = "Artemis III"
        number_of_days = 30
        break
    else:
        print("Please choose a valid mission: ")
        continue

required_oxygen = number_of_days*crew_size*oxygen_per_day
required_food = number_of_days*crew_size*food_per_day

if required_oxygen < maximum_oxygen and required_food < maximum_food:
    print("""
+--------------------------+
|     READY FOR LAUNCH!    |
+--------------------------+
    """)
else:
    print("""
+--------------------------+
|   NOT SAFE TO LAUNCH!    |
+--------------------------+
    """)

print(f"""
Mission: {mission}
Crew: {crew_size}
Required Oxygen for mission: {required_oxygen}
Required food for mission: {required_food}
""")