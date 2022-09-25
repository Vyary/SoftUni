type_of_coffee = input()
sugar = input()
number_of_drinks = int(input())
price = 0

if type_of_coffee == 'Espresso':
    if sugar == 'Without':
        price = 0.90
    elif sugar == 'Normal':
        price = 1
    elif sugar == 'Extra':
        price = 1.2
elif type_of_coffee == 'Cappuccino':
    if sugar == 'Without':
        price = 1
    elif sugar == 'Normal':
        price = 1.2
    elif sugar == 'Extra':
        price = 1.6
elif type_of_coffee == 'Tea':
    if sugar == 'Without':
        price = 0.5
    elif sugar == 'Normal':
        price = 0.6
    elif sugar == 'Extra':
        price = 0.7

total_price = price * number_of_drinks
if sugar == 'Without':
    total_price *= 0.65
if type_of_coffee == 'Espresso' and number_of_drinks >= 5:
    total_price *= 0.75
if total_price > 15:
    total_price *= 0.80

print(f"You bought {number_of_drinks} cups of {type_of_coffee} for {total_price:.2f} lv.")
