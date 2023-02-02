trip_price = float(input())
puzzles = int(input())
dolls = int(input())
teddy_bears = int(input())
minions = int(input())
trucks = int(input())

puzzle_price = 2.60
doll_price = 3
teddy_bear_price = 4.10
minion_price = 8.20
truck_price = 2

total_toys = puzzles + dolls + teddy_bears + minions + trucks
total_toys_price = (puzzles * puzzle_price) + (dolls * doll_price) + (teddy_bears * teddy_bear_price) \
                   + (minions * minion_price) + (trucks * truck_price)

if total_toys >= 50:
    total_toys_price = total_toys_price * 0.75

total_price_with_rent = total_toys_price - (total_toys_price * 0.10)
money_left = abs(total_price_with_rent - trip_price)

if total_price_with_rent >= trip_price:
    print(f"Yes! {money_left:.2f} lv left.")
elif total_price_with_rent < trip_price:
    print(f"Not enough money! {money_left:.2f} lv needed.")
