voucher_value = int(input())
purchase = input()

movie_ticket_counter = 0
other_purchase_counter = 0
movie_ticket_price = 0
other_purchase_price = 0

while purchase != 'End':
    if len(purchase) > 8:
        movie_ticket_price = ord(purchase[0]) + ord(purchase[1])
        voucher_value -= movie_ticket_price
        if voucher_value < 0:
            break
        else:
            movie_ticket_counter += 1
    elif len(purchase) <= 8:
        other_purchase_price = ord(purchase[0])
        voucher_value -= other_purchase_price
        if voucher_value < 0:
            break
        else:
            other_purchase_counter += 1

    purchase = input()

print(f"{movie_ticket_counter}")
print(f"{other_purchase_counter}")
