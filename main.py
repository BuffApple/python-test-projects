



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




expenses = [{
    "description": "Groceries",
    "amount": 25.50,
    "category": "Food"
},
    {    "description": "Groceries",
    "amount": 25.50,
    "category": "Food"}]

