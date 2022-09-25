budget = float(input())
extras = int(input())
suit_price = float(input())

decor = budget * 0.10
total_suit_price = extras * suit_price
if extras > 150:
    total_suit_price = total_suit_price * 0.90

total_price = decor + total_suit_price
diff = abs(budget - total_price)

if total_price > budget:
    print('Not enough money!')
    print(f'Wingard needs {diff:.2f} leva more.')
else:
    print('Action!')
    print(f'Wingard starts filming with {diff:.2f} leva left.')
