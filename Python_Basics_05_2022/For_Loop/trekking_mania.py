number_of_groups = int(input())
musala = 0
montblanc = 0
kilimanjaro = 0
k2 = 0
everest = 0
total_climbers = 0

for number in range(number_of_groups):
    number_of_climbers = int(input())
    total_climbers += number_of_climbers
    
    if number_of_climbers <= 5:
        musala += number_of_climbers
    elif 5 < number_of_climbers <= 12:
        montblanc += number_of_climbers
    elif 12 < number_of_climbers <= 25:
        kilimanjaro += number_of_climbers
    elif 25 < number_of_climbers <= 40:
        k2 += number_of_climbers
    elif number_of_climbers > 40:
        everest += number_of_climbers

musala_total = musala / total_climbers * 100
montblanc_total = montblanc / total_climbers * 100
kilimanjaro_total = kilimanjaro / total_climbers * 100
k2_total = k2 / total_climbers * 100
everest_total = everest / total_climbers * 100

print(f'{musala_total:.2f}%')
print(f'{montblanc_total:.2f}%')
print(f'{kilimanjaro_total:.2f}%')
print(f'{k2_total:.2f}%')
print(f'{everest_total:.2f}%')
