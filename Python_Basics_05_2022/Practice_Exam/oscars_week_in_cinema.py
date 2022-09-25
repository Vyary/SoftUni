movie = input()
seat_type = input()
tickets = int(input())

price = 0

if movie == 'A Star Is Born':
    if seat_type == 'normal':
        price = 7.5
    elif seat_type == 'luxury':
        price = 10.5
    elif seat_type == 'ultra luxury':
        price = 13.50
elif movie == 'Bohemian Rhapsody':
    if seat_type == 'normal':
        price = 7.35
    elif seat_type == 'luxury':
        price = 9.45
    elif seat_type == 'ultra luxury':
        price = 12.75
elif movie == 'Green Book':
    if seat_type == 'normal':
        price = 8.15
    elif seat_type == 'luxury':
        price = 10.25
    elif seat_type == 'ultra luxury':
        price = 13.25
elif movie == 'The Favourite':
    if seat_type == 'normal':
        price = 8.75
    elif seat_type == 'luxury':
        price = 11.55
    elif seat_type == 'ultra luxury':
        price = 13.95

total = price * tickets

print(f"{movie} -> {total:.2f} lv.")
