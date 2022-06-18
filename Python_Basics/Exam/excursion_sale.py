sea_trips = int(input())
mountain_trips = int(input())

sea_price = 680
mountain_price = 499
total = 0
sold = False

type_of_trip = input()

while type_of_trip != 'Stop':
    if type_of_trip == 'sea':
        if sea_trips > 0:
            total += sea_price
            sea_trips -= 1
    elif type_of_trip == 'mountain':
        if mountain_trips > 0:
            total += mountain_price
            mountain_trips -= 1
    if mountain_trips == 0 and sea_trips == 0:
        sold = True
        break

    type_of_trip = input()

if sold:
    print("Good job! Everything is sold.")

print(f"Profit: {total} leva.")
