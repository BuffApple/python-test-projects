# def process_users(users: list[dict[str,int | str | bool]]) -> dict[str,float | list[dict[str,int | str | bool]] | list[int | str]]:
#     eligible_users = []
#     eligible_users_names = []
#     average_age = 0
#     rejected_ids = []
#     for user in users:
#         user_id = user["id"]
#         name = user["name"]
#         age = user["age"]
#         status = user["active"]
#         if isinstance(status,bool) and isinstance(age,int):
#             if status and age >= 18:
#                 eligible_users.append(user)
#                 eligible_users_names.append(name)
#                 average_age+=age
#             else:
#                 rejected_ids.append(user_id)
#     average_age = (average_age/len(eligible_users_names) if len(eligible_users_names) else average_age)
#     return {"eligible_users": eligible_users, "names": eligible_users_names, "average_age": average_age, "rejected_ids": rejected_ids}


catalog = {
    101: {"name": "Keyboard", "price": 45.0, "stock": 4},
    102: {"name": "Mouse", "price": 20.0, "stock": 10},
    103: {"name": "Monitor", "price": 180.0, "stock": 2},
}

cart = [
    {"product_id": 101, "quantity": 2},
    {"product_id": 102, "quantity": 3},
    {"product_id": 101, "quantity": 1},
]

def calculate_cart(catalog:dict[int,dict[str,str | int | float]],cart:list[dict[str,int]]) -> dict[str,dict[str,str | int | float] | int | float | dict[str,str | int ]]:
    items = {}
    errors = {}
    for product in cart:
        pro_id = product["product_id"]
        quantity = product["quantity"]
        if pro_id in catalog:
            if catalog[pro_id]["stock"] >= quantity:
                if pro_id not in items:
                    items[pro_id]["name"] = catalog[pro_id]["name"]
                    items[pro_id]["total"] = items.get(pro_id,{}).get("total",0)
                    items[pro_id]["quantity"] = items.get(pro_id,{}).get("quantity",0) + quantity
                    total_price = quantity*catalog[pro_id]["price"]
                    items[pro_id]["total"]+=total_price


