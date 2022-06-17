number_of_product = int(input())
type_of_product = input()
delivery = input()

order_is_invalid = False
price = 0

if number_of_product > 10:
    if type_of_product == '90X130':
        price = 110
        price *= number_of_product
        if number_of_product > 60:
            price *= 0.92
        elif number_of_product > 30:
            price *= 0.95
    elif type_of_product == '100X150':
        price = 140
        price *= number_of_product
        if number_of_product > 80:
            price *= 0.90
        elif number_of_product > 40:
            price *= 0.94
    elif type_of_product == '130X180':
        price = 190
        price *= number_of_product
        if number_of_product > 50:
            price *= 0.88
        elif number_of_product > 20:
            price *= 0.93
    elif type_of_product == '200X300':
        price = 250
        price *= number_of_product
        if number_of_product > 50:
            price *= 0.86
        elif number_of_product > 25:
            price *= 0.91
else:
    order_is_invalid = True

if delivery == "With delivery":
    price += 60

if number_of_product > 99:
    price *= 0.96

if order_is_invalid:
    print("Invalid order")
else:
    print(f"{price:.2f} BGN")
