command = input()

player_name = command
points = 0

while command != 'Stop':
    current_points = 0
    for index in range(len(command)):
        score = int(input())
        if score == ord(command[index]):  # ord is used to find ASCII number
            current_points += 10
        else:
            current_points += 2

    if current_points > points:
        points = current_points
        player_name = command
    elif current_points == points:
        points = current_points
        player_name = command

    command = input()

print(f"The winner is {player_name} with {points} points!")
