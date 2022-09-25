number_of_pens = int(input())
number_of_markers = int(input())
lt_of_detergent = int(input())
discount = int(input())

price_per_pen = 5.8
price_per_marker = 7.2
price_per_lt_of_detergent = 1.2
discount_in_percentage = discount / 100

total_price_for_pens = number_of_pens * price_per_pen
total_price_for_markers = number_of_markers * price_per_marker
total_price_for_detergent = lt_of_detergent * price_per_lt_of_detergent

total_sum_before_discount = total_price_for_pens + total_price_for_markers + total_price_for_detergent
total_sum_with_discount = total_sum_before_discount - total_sum_before_discount * discount_in_percentage

print(total_sum_with_discount)
