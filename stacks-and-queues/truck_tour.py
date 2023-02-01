from collections import deque

number_of_pumps = int(input())

circle_is_not_completed = True
gas_tank = 0
index = 0

pumps = deque([])

for pump in range(number_of_pumps):
    pumps.append([int(number) for number in input().split()])

while circle_is_not_completed:
    count = 0

    for pump in range(number_of_pumps):
        petrol, distance = pumps[pump]

        gas_tank += petrol
        if gas_tank >= distance:
            gas_tank -= distance
            count += 1
            if count == number_of_pumps:
                circle_is_not_completed = False
                break
    else:
        pumps.rotate(-1)
        gas_tank = 0
        index += 1

print(index)


"""                     Task:
There is a circle road with N petrol pumps. The petrol pumps are numbered 0 to (N-1)
(both inclusive). For each petrol pump, you will receive two pieces of information
(separated by a single space):
-	The amount of petrol the petrol pump will give you
-	The distance from that petrol pump to the next petrol pump (kilometers)
You are a truck driver, and you want to go all around the circle. You know that the
truck consumes 1 liter of petrol per 1 kilometer, and its tank has infinite
petrol capacity.
In the beginning, the tank is empty, but you start your journey at a petrol pump so
you can fill it with the given amount of petrol.
Your task is to calculate the first petrol pump from where the truck will be able to
complete the circle. You never miss filling its tank at a petrol pump.
Input
•	On the first line, you will receive the number of petrol pumps - N
•	On the next N lines, you will receive the amount of petrol that each petrol pump
will give and the distance between that petrol pump and the next petrol pump,
separated by a single space
Output
•	An integer which will be the smallest index of a petrol pump from which you can
start the tour
Constraints
•	1 ≤ N ≤ 1000001
•	1 ≤ amount of petrol, distance ≤ 1000000000
•	You will always have at least one point from where the truck will be able to
complete the circle

Examples:
Input:          Output:
3               1
1 5
10 3
3 4

5               0
22 5
14 10
52 7
21 12
36 9
"""
