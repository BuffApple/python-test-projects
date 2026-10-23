



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



expenses = [{
    "description": "Groceries",
    "amount": 25.50,
    "category": "Food"
},
    {    "description": "Groceries",
    "amount": 25.50,
    "category": "Food"}]

print(summerize_by_category())