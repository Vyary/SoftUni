# Write a program that keeps the information about products and their prices.
# Each product has a name, a price, and a quantity:
# •	If the product doesn't exist yet, add it with its starting quantity.
# •	If you receive a product, which already exists,
# increases its quantity by the input quantity and if its price is different, replace the price as well.
# You will receive products' names, prices, and quantities on new lines. Until you receive the command "buy",
# keep adding items. Finally, print all items with their names and the total price of each product.
# Input
# •	Until you receive "buy", the products will be coming in the format: "{name} {price} {quantity}".
# •	The product data is always delimited by a single space.
# Output
# •	Print information about each product in the following format:
# "{product_name} -> {total_price}"
# •	Format the total price to the 2nd digit after the decimal separator.

inventory = {}

while True:
    entry = input().split(' ')
    if entry[0] == 'buy':
        break
    product, price, quantity = entry
    if product not in inventory:
        inventory[product] = [0.0, 0]
    inventory[product][0] = float(price)
    inventory[product][1] += int(quantity)

for product, price_and_quantity in inventory.items():
    total_price = price_and_quantity[0] * price_and_quantity[1]
    print(f"{product} -> {total_price:.2f}")
