budget = float(input())
number_of_nights = int(input())
price_per_night = float(input())
percent = int(input())

if number_of_nights > 7:
    price_per_night *= 0.95

total_price = number_of_nights * price_per_night
extra_spending = budget * (percent / 100)
end_price = total_price + extra_spending

diff = abs(budget - end_price)

if end_price > budget:
    print(f"{diff:.2f} leva needed.")
else:
    print(f"Ivanovi will be left with {diff:.2f} leva after vacation.")
