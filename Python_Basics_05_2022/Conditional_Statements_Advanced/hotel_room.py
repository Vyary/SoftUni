month = input()
nights = int(input())

studio = 0
apartment = 0

if month == 'May' or month == 'October':
    studio = 50
    apartment = 65
if month == 'June' or month == 'September':
    studio = 75.20
    apartment = 68.70
if month == 'July' or month == 'August':
    studio = 76
    apartment = 77

price_for_studio = studio * nights
price_for_apartment = apartment * nights

if nights > 14:
    price_for_apartment *= 0.90
if nights > 14 and (month == 'June' or month == 'September'):
    price_for_studio *= 0.80
elif nights > 14 and (month == 'May' or month == 'October'):
    price_for_studio *= 0.70
elif nights > 7 and (month == 'May' or month == 'October'):
    price_for_studio *= 0.95

print(f"Apartment: {price_for_apartment:.2f} lv.")
print(f"Studio: {price_for_studio:.2f} lv.")
