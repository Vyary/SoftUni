hour = int(input())
minutes = int(input())

plus_15_minutes = (minutes + 15) % 60
total_hour = hour + ((minutes + 15) // 60)

if total_hour % 24 == 0:
    total_hour = 0

print(f'{total_hour}:{plus_15_minutes:02d}')
