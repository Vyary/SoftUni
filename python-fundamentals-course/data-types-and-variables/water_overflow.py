# You have a water tank with a capacity of 255 liters. On the first line,
# you will receive n – the number of lines, which will follow. On the following n lines,
# you will receive liters of water (integers), which you should pour into your tank.
# If the capacity is not enough, print "Insufficient capacity!" and continue reading the next line.
# On the last line, print the liters in the tank.

water_tank_capacity = 255
tank_filled_to = 0

number_of_fills = int(input())

for fill in range(number_of_fills):
    liters_to_add = int(input())
    if tank_filled_to + liters_to_add <= water_tank_capacity:
        tank_filled_to += liters_to_add
    else:
        print('Insufficient capacity!')

print(tank_filled_to)
