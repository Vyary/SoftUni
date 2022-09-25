name_of_city = input()
type_of_package = input()
vip = input()
days_of_stay = int(input())
price = 0

is_vip = False
incorrect_package = False
incorrect_city = False
days_of_stay_are_negative = False

if days_of_stay < 1:
    days_of_stay_are_negative = True
elif days_of_stay > 7:
    days_of_stay -= 1

if name_of_city == 'Bansko' or name_of_city == 'Borovets':
    if type_of_package == 'noEquipment':
        price = 80
        if vip == 'yes':
            price *= 0.95
    elif type_of_package == 'withEquipment':
        price = 100
        if vip == 'yes':
            price *= 0.90
    else:
        incorrect_package = True
elif name_of_city == 'Varna' or name_of_city == 'Burgas':
    if type_of_package == 'noBreakfast':
        price = 100
        if vip == 'yes':
            price *= 0.93
    elif type_of_package == 'withBreakfast':
        price = 130
        if vip == 'yes':
            price *= 0.88
    else:
        incorrect_package = True
else:
    incorrect_city = True

total_price = price * days_of_stay

if days_of_stay_are_negative:
    print(f"Days must be positive number!")
elif incorrect_city or incorrect_package:
    print(f"Invalid input!")
else:
    print(f"The price is {total_price:.2f}lv! Have a nice time!")
