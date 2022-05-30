type_of_flowers = input()
number_of_flowers = int(input())
budget = int(input())

roses = 5
dahlias = 3.80
tulips = 2.80
narcissus = 3
gladiolus = 2.50

price = 0
inc_or_reduce = 1

if type_of_flowers == 'Roses':
    price = roses * number_of_flowers
    if number_of_flowers > 80:
        inc_or_reduce = 0.90
elif type_of_flowers == 'Dahlias':
    price = dahlias * number_of_flowers
    if number_of_flowers > 90:
        inc_or_reduce = 0.85
elif type_of_flowers == 'Tulips':
    price = tulips * number_of_flowers
    if number_of_flowers > 80:
        inc_or_reduce = 0.85
elif type_of_flowers == 'Narcissus':
    price = narcissus * number_of_flowers
    if number_of_flowers < 120:
        inc_or_reduce = 1.15
elif type_of_flowers == 'Gladiolus':
    price = gladiolus * number_of_flowers
    if number_of_flowers < 80:
        inc_or_reduce = 1.20

end_price = price * inc_or_reduce
difference = abs(end_price - budget)

if budget >= end_price:
    print(f"Hey, you have a great garden with {number_of_flowers} {type_of_flowers} and {difference:.2f} leva left.")
elif budget < end_price:
    print(f"Not enough money, you need {difference:.2f} leva more.")
