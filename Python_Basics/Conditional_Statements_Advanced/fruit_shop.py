product = input()
day_of_the_week = input()
quantity = float(input())

price = 0
product_is_valid = True
day_is_valid = True

if day_of_the_week == 'Monday' \
        or day_of_the_week == 'Tuesday' \
        or day_of_the_week == 'Wednesday' \
        or day_of_the_week == 'Thursday' \
        or day_of_the_week == 'Friday':
    if product == 'banana':
        price = 2.50
    elif product == 'apple':
        price = 1.20
    elif product == 'orange':
        price = 0.85
    elif product == 'grapefruit':
        price = 1.45
    elif product == 'kiwi':
        price = 2.70
    elif product == 'pineapple':
        price = 5.50
    elif product == 'grapes':
        price = 3.85
    else:
        product_is_valid = False
elif day_of_the_week == 'Saturday' \
        or day_of_the_week == 'Sunday':
    if product == 'banana':
        price = 2.70
    elif product == 'apple':
        price = 1.25
    elif product == 'orange':
        price = 0.90
    elif product == 'grapefruit':
        price = 1.60
    elif product == 'kiwi':
        price = 3.00
    elif product == 'pineapple':
        price = 5.60
    elif product == 'grapes':
        price = 4.20
    else:
        product_is_valid = False
else:
    day_is_valid = False

total_price = price * quantity
if product_is_valid and day_is_valid:
    print(f'{total_price:.2f}')
else:
    print('error')