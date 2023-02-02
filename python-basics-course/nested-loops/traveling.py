destination = input()

while destination != 'End':
    trip_cost = float(input())
    while trip_cost > 0:
        saved = float(input())
        trip_cost -= saved

    print(f"Going to {destination}!")

    destination = input()
