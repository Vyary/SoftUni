nylon = int(input())
paint = int(input())
paint_thinner = int(input())
work_hours = int(input())

price_per_nylon = 1.5
price_per_paint = 14.5
price_per_paint_thinner = 5

total_price_of_nylon = (nylon + 2) * price_per_nylon
total_price_of_paint = (paint * 1.10) * price_per_paint
total_price_of_paint_thinner = paint_thinner * price_per_paint_thinner

total_price_of_supplies = total_price_of_nylon + total_price_of_paint + total_price_of_paint_thinner + 0.40

workers_payment = total_price_of_supplies * 0.30

total_sum = total_price_of_supplies + (workers_payment * work_hours)

print(total_sum)
