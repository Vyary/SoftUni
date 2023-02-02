# Write a program that calculates the total cost of bought furniture.
# You will be given information about each purchase on separate lines until you receive the command "Purchase".
# Valid information should be in the format: ">>{furniture_name}<<{price}!{quantity}". The price could be a
# floating-point or integer number. You should store the names of the furniture and the total price.
# In the end, print the name of each bought furniture and the total cost, formatted to the second decimal point:
# "Bought furniture:
# {1st name}
# {2nd name}
# …
# {N name}
# Total money spend: {total_cost}"

import re

command = input()
pattern = r'>>([A-Za-z]+)<<([\d]+.?\d+)!(\d+)'
purchases = []
total_price = 0

while command != 'Purchase':
    matches = re.search(pattern, command)
    if matches:
        purchase, price, count = matches.groups()
        purchases.append(purchase)
        total_price += float(price) * int(count)
    command = input()

print('Bought furniture:')
for purchase in purchases:
    print(purchase)
print(f'Total money spend: {total_price:.2f}')
