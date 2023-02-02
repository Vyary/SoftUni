# Tony and Andi love playing in the snow and having snowball fights,
# but they always argue about who makes the best snowballs.
# They have decided to involve you in their fray by writing a program that calculates snowball data and
# outputs the best snowball value.
# You will receive N – an integer, the number of snowballs being made by Tony and Andi.
# On the following lines, you will receive 3 inputs for each snowball:
# •	The weight of the snowball (integer).
# •	The time needed for the snowball to get to its target (integer).
# •	The quality of the snowball (integer).
# For each snowball, you must calculate its value by the following formula:
# (snowball_weight / snowball_time) ** snowball_quality
# In the end, you must print the highest calculated value of a snowball.
# Input
# •	On the first input line, you will receive N – the number of snowballs.
# •	On the next N*3 input lines, you will be receiving data about each snowball.
# Output
# •	You need to print the highest calculated snowball's value in the format:
# "{snowball_weight} : {snowball_time} = {snowball_value} ({snowball_quality})"
# Constraints
# •	The number of snowballs (N) will be an integer in range [0, 100].
# •	The weight is an integer in the range [0, 1000].
# •	The time is an integer in the range [1, 500].
# •	The quality is an integer in the range [0, 100].
# Examples
# Input	Output
# 2
# 10
# 2
# 3
# 5
# 5
# 5	10 : 2 = 125 (3)

number_of_snowballs = int(input())
best_snowball_weight = 0
best_snowball_travel_time = 0
best_snowball_score = 0
best_snowball_quality = 0

for snowball in range(number_of_snowballs):
    snowball_weight = int(input())
    travel_time = int(input())
    snowball_quality = int(input())
    snowball_score = (snowball_weight / travel_time) ** snowball_quality
    if snowball_score > best_snowball_score:
        best_snowball_score = int(snowball_score)
        best_snowball_weight = snowball_weight
        best_snowball_travel_time = travel_time
        best_snowball_quality = snowball_quality

print(f'{best_snowball_weight} : {best_snowball_travel_time} = {best_snowball_score} ({best_snowball_quality})')
