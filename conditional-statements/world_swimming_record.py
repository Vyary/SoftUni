from math import floor

record_in_seconds = float(input())
range_in_meters = float(input())
seconds_per_1_meter = float(input())

water_resistance = floor(range_in_meters / 15) * 12.5

attempt = range_in_meters * seconds_per_1_meter + water_resistance

diff = abs(attempt - record_in_seconds)

if attempt < record_in_seconds:
    print(f"Yes, he succeeded! The new world record is {attempt:.2f} seconds.")
else:
    print(f"No, he failed! He was {diff:.2f} seconds slower.")