trip_price = float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

puzzles_price = puzzles * 2.60
dolls_price = dolls * 3
bears_price = bears * 4.10
minions_price = minions * 8.20
trucks_price = trucks * 2

total_price = puzzles_price + dolls_price + bears_price + minions_price + trucks_price
number_of_toys = puzzles + dolls + bears + minions + trucks

if number_of_toys >= 50:
    total_price = total_price * 0.75

total_price = total_price - (total_price * 0.10)

diff = abs(total_price - trip_price)

if total_price > trip_price:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")
