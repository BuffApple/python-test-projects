size = input("""What pizza size do you want? 
(small: 6$)
(medium: 8$)
(large: 10$)
""").lower()

price = 0

match size:
    case "small":
        price+=6
    case "medium":
        price+=8
    case "large":
        price+=10
    case _:
        print("Ninja we dont have that size!")
        exit()

base = input("""What kind of base?
(Classic: 0$)
(Thin and Crispy: 1$)
(Deep pan: 2$)
""").lower()

match base:
    case "classic":
        pass
    case "thin and crispy":
        price+=1
    case "deep pan":
        price+=2
    case _:
        print("fuck you and your pizza")
        exit()

try:
    toppings = int(input("How many toppings to add?(1.5$ for each): "))
except ValueError:
    print("Nigga you have to choose a number!")
    exit()
if toppings<0:
    print("Bitch are you forreal")
    exit()
price+= toppings*1.5

discount = input("Enter coupon:(optional) ")
if discount == "ninja":
    print("Coupon detected! 20% off total!")
    price*=0.8
else:
    print("invalid coupon!")

print(f"""Your pizza:
size: {size}
base: {base}
toppings: {toppings}
total price: {price}
""")
