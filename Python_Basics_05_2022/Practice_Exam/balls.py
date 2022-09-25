number_of_balls = int(input())

points = 0
red_balls = 0
orange_balls = 0
yellow_balls = 0
white_balls = 0
other_colors = 0
divides_from_black_balls = 0

for balls in range(number_of_balls):
    ball = input()
    if ball == 'red':
        points += 5
        red_balls += 1
    elif ball == 'orange':
        points += 10
        orange_balls += 1
    elif ball == 'yellow':
        points += 15
        yellow_balls += 1
    elif ball == 'white':
        points += 20
        white_balls += 1
    elif ball == 'black':
        points = int(points / 2)
        divides_from_black_balls += 1
    else:
        other_colors += 1

print(f"Total points: {points}")
print(f"Red balls: {red_balls}")
print(f"Orange balls: {orange_balls}")
print(f"Yellow balls: {yellow_balls}")
print(f"White balls: {white_balls}")
print(f"Other colors picked: {other_colors}")
print(f"Divides from black balls: {divides_from_black_balls}")
