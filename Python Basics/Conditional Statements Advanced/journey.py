budget = float(input())
season = input()

trip_budget = 0
destination = ''
place = ''

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        place = 'Camp'
        trip_budget = budget * 0.30
    elif season == 'winter':
        place = 'Hotel'
        trip_budget = budget * 0.70
elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        place = 'Camp'
        trip_budget = budget * 0.40
    elif season == 'winter':
        place = 'Hotel'
        trip_budget = budget * 0.80
elif budget > 1000:
    destination = 'Europe'
    place = 'Hotel'
    trip_budget = budget * 0.90

print(f'Somewhere in {destination}')
print(f'{place} - {trip_budget:.2f}')
