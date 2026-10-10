sports = {
    "team" : {
        "indoor":{
            "contact": ["basketball"],
            "non-contact": ["volleyball"]
        },
        "outdoor":{
            "contact": ["football","rugby"],
            "non-contact": ["cricket","volleyball"]
        }
    },
    "individual": {
        "indoor":{
            "contact": ["swimming","badminton"],
            "non-contact": ["tennis"]
        },
        "outdoor":{
            "contact": ["swimming"],
            "non-contact": ["surfing","running","tennis"]
        }
    }
}


is_teams = input("Do you like team sports? ").lower()

match is_teams:
    case "yes":
        is_teams = "team"
    case "no":
        is_teams = "individual"
    case _:
        print("Invalid response!")
        exit()

is_outdoor = input("Do you like outdoor activities? ").lower()

match is_outdoor:
    case "yes":
        is_outdoor = "outdoor"
    case "no":
        is_outdoor = "indoor"
    case _:
        print("Invalid response!")
        exit()

is_contact = input("Do you like contact activities? ").lower()

match is_contact:
    case "yes":
        is_contact = "contact"
    case "no":
        is_contact = "non-contact"
    case _:
        print("Invalid response!")
        exit()

print("Suggested sports: ")
for item in sports[is_teams][is_outdoor][is_contact]:
    print(item)

