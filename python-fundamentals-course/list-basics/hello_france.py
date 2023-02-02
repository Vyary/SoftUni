# You want to go to France by train, and the train ticket costs exactly 150$. You do not have enough money,
# so you decide to buy some items with your budget and then sell them at a higher price – with a 40% markup.
# You will receive a collection of items and a budget in the following format:
# {type->price|type->price|type->price……|type->price}
# {budget}
# The prices for each of the types cannot exceed a specific price, which is given below:
# Type	Maximum Price
# Clothes	50.00
# Shoes	35.00
# Accessories	20.50
# If a price for a particular item is higher than the maximum price, don't buy it. Every time you buy an item,
# you have to reduce the budget with its price value. If you don't have enough money for it, you can't buy it.
# Buy as many items as you can.
# Next, you should increase the price of each item you have successfully bought by 40% and then sell it.
# Calculate if the budget after selling all the items is enough for buying the train ticket.
# Input / Constraints
# •	On the 1st line, you will receive the items with their prices in the format described above – real numbers in
# the range [0.00……1000.00]
# •	On the 2nd line, you are going to be given the budget – a real number in the range [0.0….1000.0]
# Output
# •	First, print the list with the bought item’s new prices, formatted to the second decimal point in
# the following format:
# "{price1} {price2} {price3} … {priceN}"
# •	Second, print the profit, formatted to the second decimal point in the following format:
# "Profit: {profit}"
# •	Finally:
# o	If the budget is enough for buying the train ticket, print: "Hello, France!"
# o	Otherwise, print: "Not enough money."

import re

items_to_buy = re.split('[->|]', input())
budget = int(input())
total_gross_sales = 0
sold_prices = []
start_budget = budget
able_to_buy_ticket = False

for item_index in range(0, len(items_to_buy), 3):
    item = items_to_buy[item_index]
    price = float(items_to_buy[item_index + 2])
    if item == 'Clothes' and price <= 50 and (budget - price) >= 0:
        budget -= price
        sell_price = price * 1.40
        total_gross_sales += sell_price
        sold_prices.append(f'{sell_price:.2f}')
    elif item == 'Shoes' and price <= 35 and (budget - price) >= 0:
        budget -= price
        sell_price = price * 1.40
        total_gross_sales += sell_price
        sold_prices.append(f'{sell_price:.2f}')
    elif item == 'Accessories' and price <= 20.50 and (budget - price) >= 0:
        budget -= price
        sell_price = price * 1.40
        total_gross_sales += sell_price
        sold_prices.append(f'{sell_price:.2f}')

profit = total_gross_sales - start_budget + budget
if total_gross_sales + budget >= 150:
    able_to_buy_ticket = True

print(*sold_prices, sep=' ')
print(f"Profit: {profit:.2f}")
if able_to_buy_ticket:
    print('Hello, France!')
else:
    print("Not enough money.")
