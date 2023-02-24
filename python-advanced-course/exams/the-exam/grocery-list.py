def shop_from_grocery_list(budget, grocery_list, *products):
    purchased_products = []
    total_cost = 0

    for product, price in products:
        if product not in grocery_list:
            continue

        if product in purchased_products:
            continue

        if budget < price:
            break

        purchased_products.append(product)
        total_cost += price
        budget -= price

    if len(purchased_products) == len(grocery_list):
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        for product in purchased_products:
            grocery_list.remove(product)
        return f"You did not buy all the products. Missing products: {', '.join(grocery_list)}."
