profit_wanna_be = float(input())
drink = input()
total = 0
end_price = 0
profit_reached = False

while drink != "Party!":
    number_of_drinks = int(input())
    drink_price = len(drink)
    end_price = drink_price * number_of_drinks
    if end_price % 2 != 0:
        end_price *= 0.75
    total += end_price
    if total >= profit_wanna_be:
        profit_reached = True
        break
    drink = input()

if profit_reached:
    print("Target acquired.")
else:
    diff = abs(profit_wanna_be - total)
    print(f"We need {diff:.2f} leva more.")
print(f"Club income - {total:.2f} leva.")
