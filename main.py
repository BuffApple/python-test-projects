import json

def add_expense(expenses: list[dict[str,float | int| str]]) -> None:

    description = input("Enter expense description: ")
    if not len(description):
        description = "No description found"

    amount = 0
    while True:
        try:
            amount = float(input("Enter expense amount: "))
            if amount < 0:
                print("Please add a valid positive number!")
                continue
            break
        except ValueError:
            print("Please enter a valid number!")

    category = input("Please enter category: ")
    if not len(category):
        category = "No category chosen"

    expenses.append({"description": description,"amount": amount,"category" : category})
    print("Done!")
    return

def display_expenses(expenses: list[dict[str,float | int| str]]) -> None:
    num = 1
    for expense in expenses:
        description = expense["description"]
        amount = expense["amount"]
        category = expense["category"]
        print(f"""Expense {num}:
    Description: {description}
    amount: {amount}
    category: {category}\n""")
        num+=1

def calculate_total_spending(expenses: list[dict[str,float | int| str]]) -> float | int:
    total = 0.0
    for expense in expenses:
        total+=expense["amount"]
    return total

def summerize_by_category(expenses: list[dict[str,float | int| str]]) -> dict[str,int | float]:
    categories = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]
        if isinstance(amount,int | float):
            categories[category] = categories.get(category,0.0) + amount

    return categories

def find_largest_expense(expenses: list[dict[str,float | int| str]]) -> dict[str,str | int | float] :
    largest_expense : dict[str,str | int | float] = {}
    largest_num = -1

    for expense in expenses:
        amount = expense["amount"]
        if isinstance(amount,float | int) and amount > largest_num:
            largest_num = amount
            largest_expense = expense

    return largest_expense

def save_file(expenses: list[dict[str,float | int| str]]) -> None: #I wanted to return a boolean value here so we have a clearer look if the saving worked or not but since
                                                                    # we are not dealing with errors yet ill return None
    with open("expenses.json","w") as file:
        json.dump(expenses,file)

def load_file():
    try:
        with open("expenses.json","r") as file:
             data = json.load(file)
             return data
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return None



def menu(expenses):
    while True:
        choice = input("""---Expense Tracker 0.1---
\t1.Add expense
\t2.Display expenses
\t3.Calculate total spending
\t4.Summerize by category
\t5.Find largest expense
\t6.Save expenses
\t7.Load expenses
\t0.Exit\n\t""").lower().rstrip()

        if choice not in ["add","1","add expense","save","6","save expenses" ,"load","7","load expenses"] and len(expenses) <= 0:
            print("Your expense list is empty!")

        match choice:
            case a if a in ["add","1","add expense"]:
                add_expense(expenses)

            case b if b in ["display","2","display expenses"]:
                display_expenses(expenses)

            case c if c in ["calculate total","calculate","3","calculate total spending"]:
                print(f"Total spending: {calculate_total_spending(expenses)}")

            case d if d in ["summerize","summerize by category","4"] :
                categories = summerize_by_category(expenses)
                for category,value in categories.items():
                    print(f"Category {category}: {value}")

            case e if e in ["find","find largest","find largest expense","5"]:
                largest_expense = find_largest_expense(expenses)
                for key,value in largest_expense.items():
                    print(key,value,sep=": ")

            case f if f in ["save","save expenses","6"]:
                 save_file(expenses)

            case g if g in ["load","load expenses","7"]:
                data = load_file()
                if data is None:
                    print("Unable to load data!")
                else:
                    expenses = data

            case h if h in ["exit","0"]:
                exit()

            case _:
                print("Please enter a valid command!\n")

        stop = input("Press enter to continue...\n")





expenses = []
menu(expenses)

