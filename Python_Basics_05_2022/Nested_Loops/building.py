number_of_floors = int(input())
number_of_apartments = int(input())
floor_type = ''

for floor in range(number_of_floors, 0, -1):
    for apartment in range(number_of_apartments):
        if floor == number_of_floors:
            floor_type = 'L'
        elif floor % 2 == 0:
            floor_type = 'O'
        else:
            floor_type = 'A'
        print(f'{floor_type}{floor}{apartment}', end=' ')
    print()
