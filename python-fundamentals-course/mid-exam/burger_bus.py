number_of_cities = int(input())
profit = 0
city_profit = 0

for city in range(1, number_of_cities + 1):
    city_name = input()
    earned_money = float(input())
    expenses = float(input())

    if city % 3 == 0 and not city % 5 == 0:
        expenses *= 1.5
    if city % 5 == 0:
        earned_money *= 0.9

    city_profit = earned_money - expenses
    profit += city_profit
    print(f"In {city_name} Burger Bus earned {city_profit:.2f} leva.")

print(f"Burger Bus total profit: {profit:.2f} leva.")
