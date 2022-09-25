budget = int(input())
season = input()
number_of_fishermen = int(input())

price = 0

if number_of_fishermen <= 6:
    if season == 'Spring':
        price = 3000 * 0.90
        if number_of_fishermen % 2 == 0:
            price = price * 0.95
    elif season == 'Summer':
        price = 4200 * 0.90
        if number_of_fishermen % 2 == 0:
            price = price * 0.95
    elif season == 'Autumn':
        price = 4200 * 0.90
    elif season == 'Winter':
        price = 2600 * 0.90
        if number_of_fishermen % 2 == 0:
            price = price * 0.95
elif 7 <= number_of_fishermen <= 11:
    if season == 'Spring':
        price = 3000 * 0.85
        if number_of_fishermen % 2 == 0:
            price = price * 0.95
    elif season == 'Summer':
        price = 4200 * 0.85
        if number_of_fishermen % 2 == 0:
            price = price * 0.95
    elif season == 'Autumn':
        price = 4200 * 0.85
    elif season == 'Winter':
        price = 2600 * 0.85
        if number_of_fishermen % 2 == 0:
            price = price * 0.95
elif number_of_fishermen > 12:
    if season == 'Spring':
        price = 3000 * 0.75
        if number_of_fishermen % 2 == 0:
            price = price * 0.95
    elif season == 'Summer':
        price = 4200 * 0.75
        if number_of_fishermen % 2 == 0:
            price = price * 0.95
    elif season == 'Autumn':
        price = 4200 * 0.75
    elif season == 'Winter':
        price = 2600 * 0.75
        if number_of_fishermen % 2 == 0:
            price = price * 0.95

difference = abs(budget - price)
if budget >= price:
    print(f"Yes! You have {difference:.2f} leva left.")
elif budget < price:
    print(f"Not enough money! You need {difference:.2f} leva.")
