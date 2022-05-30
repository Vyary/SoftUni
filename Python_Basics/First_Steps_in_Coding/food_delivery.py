number_of_chicken_menus = int(input())
number_of_fish_menus = int(input())
number_of_veggie_menus = int(input())

price_per_chicken_menu = 10.35
price_per_fish_menu = 12.4
price_per_veggie_menu = 8.15

total_price_for_chicken = number_of_chicken_menus * price_per_chicken_menu
total_price_for_fish = number_of_fish_menus * price_per_fish_menu
total_price_for_veggie = number_of_veggie_menus * price_per_veggie_menu

total_price_of_menus = total_price_for_chicken + total_price_for_fish + total_price_for_veggie

deserts = total_price_of_menus * 0.20

total_sum = total_price_of_menus + deserts + 2.5

print(total_sum)
