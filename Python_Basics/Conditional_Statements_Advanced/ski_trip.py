rent_days = int(input())
type_of_rent = input()
impression = input()

room_for_one = 18
apartment = 25
president_apartment = 35
price = 0
nights = rent_days - 1

if type_of_rent == 'room for one person':
    price = room_for_one * nights
elif type_of_rent == 'apartment':
    if rent_days < 10:
        price = (apartment * nights) * 0.70
    elif 10 <= rent_days <= 15:
        price = (apartment * nights) * 0.65
    elif rent_days > 15:
        price = (apartment * nights) * 0.50
elif type_of_rent == 'president apartment':
    if rent_days < 10:
        price = (president_apartment * nights) * 0.90
    elif 10 <= rent_days <= 15:
        price = (president_apartment * nights) * 0.85
    elif rent_days > 15:
        price = (president_apartment * nights) * 0.80

if impression == 'positive':
    price *= 1.25
elif impression == 'negative':
    price *= 0.90

print(f'{price:.2f}')
