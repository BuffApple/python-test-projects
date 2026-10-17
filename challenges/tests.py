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
    {"product_id": 102, "quantity": 1},
    {"product_id": 101, "quantity": 1},
]

def calculate_cart(catalog:dict[int,dict[str,str | int | float]],cart:list[dict[str,int]]) -> dict[str,dict[str,str | int | float] | int | float | list[dict[str,str | int ]]]:
    found_ids = []
    combined_cart = []

    for item in cart:
        pro_id = item["product_id"]
        quantity = item["quantity"]
        if pro_id not in found_ids:
            found_ids.append(pro_id)
            combined_cart.append(item)
        else:
            for product in combined_cart:
                if product["product_id"] == pro_id:
                    product["quantity"] += quantity



    items = {}
    total = 0
    errors = []
    for product in combined_cart:
        pro_id = product["product_id"]
        quantity = product["quantity"]
        if pro_id in catalog:
            if isinstance(quantity,int) and 0 < quantity <= catalog[pro_id]["stock"]:
                catalog[pro_id]["stock"]-=quantity
                total+= quantity*catalog[pro_id]["price"]
                if pro_id not in items:
                    items[pro_id] = items.get(pro_id,{})
                    items[pro_id]["name"] = catalog[pro_id]["name"]
                    items[pro_id]["subtotal"] = items.get(pro_id,{}).get("subtotal",0)
                    items[pro_id]["quantity"] = items.get(pro_id,{}).get("quantity",0) + quantity
                    total_price = quantity*catalog[pro_id]["price"]
                    items[pro_id]["subtotal"]+=total_price

                else:
                    total_price = quantity*catalog[pro_id]["price"]
                    items[pro_id]["subtotal"]+=total_price
                    items[pro_id]["quantity"]+=quantity
            else:
                item_name = catalog[pro_id]["name"]
                if quantity <= 0:
                    refused_item = {"name": item_name, "id": pro_id, "quantity": quantity,"reason_of_rejection": "Invalid input!"}
                    errors.append(refused_item)
                else:
                    refused_item = {"name" : item_name,"id": pro_id,"quantity": quantity,"reason_of_rejection":"Not enough items in stock!"}
                    errors.append(refused_item)
        else:
            refused_item = {"id": pro_id, "quantity": quantity,"reason_of_rejection": "Item not found!"}
            errors.append(refused_item)

    return {"items": items,"total":total,"errors":errors}

print(calculate_cart(catalog,cart))


