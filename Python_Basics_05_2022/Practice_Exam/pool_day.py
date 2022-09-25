from math import ceil

number_of_people = int(input())
price = float(input())
deck_chair_price = float(input())
umbrella_price = float(input())

total_price_for_entry = number_of_people * price
total_price_for_decks = ceil((number_of_people * 0.75)) * deck_chair_price
total_price_for_umbrellas = ceil((number_of_people / 2)) * umbrella_price

total_price = total_price_for_entry + total_price_for_decks + total_price_for_umbrellas
print(f'{total_price:.2f} lv.')
