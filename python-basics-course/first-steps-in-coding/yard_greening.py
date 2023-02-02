square_meters = float(input())
price_per_square_meters = 7.61
discount = 18
discount_percentage = discount / 100
price_before_discount = square_meters * price_per_square_meters
final_price = price_before_discount - price_before_discount * discount_percentage
saved = price_before_discount * discount_percentage
print(f"The final price is: {final_price} lv.")
print(f"The discount is: {saved} lv.")
