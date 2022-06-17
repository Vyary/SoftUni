weight_price_more_than_20 = float(input())
weight = float(input())
days_before_travel = int(input())
number_of_bags = int(input())

price = 0

if weight < 10:
    price = weight_price_more_than_20 * 0.20
    if days_before_travel > 30:
        price = price + price * 0.10
    elif 7 <= days_before_travel <= 30:
        price = price + price * 0.15
    elif days_before_travel < 7:
        price = price + price * 0.40
elif 10 <= weight <= 20:
    price = weight_price_more_than_20 * 0.50
    if days_before_travel > 30:
        price = price + price * 0.10
    elif 7 <= days_before_travel <= 30:
        price = price + price * 0.15
    elif days_before_travel < 7:
        price = price + price * 0.40
elif weight > 20:
    price = weight_price_more_than_20
    if days_before_travel > 30:
        price = price + price * 0.10
    elif 7 <= days_before_travel <= 30:
        price = price + price * 0.15
    elif days_before_travel < 7:
        price = price + price * 0.40

total = price * number_of_bags

print(f"The total price of bags is: {total:.2f} lv.")
