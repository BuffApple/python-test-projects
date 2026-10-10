blue_bin = []
green_bin = []
gray_bin = []
brown_bin = []
black_bin = []

def print_items(binn):
    for item in binn:
        print(item)

while True:
    choice = input("""What do you want to do?(Enter numbers)
1.Search bins like a raccoon
2.Throw away an item
""")

    if choice == "1":
        binn = input("""Which bin to search? (Enter numbers):
1.Blue bin
2.Green bin
3.Gray bin
4.Brown bin
5.Black bin
""")

        match binn:
            case "1":
                if blue_bin:
                    print("Items found: ")
                    print_items(blue_bin)
                else:
                    print("Bin is empty!")
            case "2":
                if green_bin:
                    print("Items found: ")
                    print_items(green_bin)
                else:
                    print("Bin is empty!")
            case "3":
                if gray_bin:
                    print("Items found: ")
                    print_items(gray_bin)
                else:
                    print("Bin is empty!")
            case "4":
                if brown_bin:
                    print("Items found: ")
                    print_items(brown_bin)
                else:
                    print("Bin is empty!")
            case "5":
                if black_bin:
                    print("Items found: ")
                    print_items(black_bin)
                else:
                    print("Bin is empty!")
            case _:
                print("Please enter a valid number!")

    elif choice == "2":
        item = input("What kind of garbage are you holding? ").lower()

        if item in ["plastic", "plastic film", "glass bottle", "drink carton","can"]:
            print("Your garbage belongs in the blue bin!")
            blue_bin.append(item)

        elif item in ["paper", "cardboard", "book" ,"cardboard packaging"]:
            print("Your garbage belongs in the green bin!")
            green_bin.append(item)
        elif item in ["food waste", "plate scrapings", "mouldy food", "pet food", "tea bag" , "coffee ground"]:
            print("Your garbage belongs in the gray bin!")
            gray_bin.append(item)

