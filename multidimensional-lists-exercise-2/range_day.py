RANGE_SIZE = 5

shooting_range = []

current_position = []

total_targets = 0
total_targets_shot = 0
shot_targets_positions = []

directions = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}

for row in range(RANGE_SIZE):
    shooting_range.append(input().split())

    if "A" in shooting_range[row]:
        current_position = [row, shooting_range[row].index("A")]
        shooting_range[current_position[0]][current_position[1]] = "."
    if "x" in shooting_range[row]:
        total_targets += int(shooting_range[row].count("x"))

number_of_commands = int(input())

for _ in range(number_of_commands):
    command, direction, *steps = input().split()

    if command == "move":
        row, col = (
            current_position[0] + directions[direction][0] * int(steps[0]),
            current_position[1] + directions[direction][1] * int(steps[0]),
        )

        if (
            0 <= row < RANGE_SIZE
            and 0 <= col < RANGE_SIZE
            and shooting_range[row][col] == "."
        ):
            current_position = [row, col]

    elif command == "shoot":
        row, col = (
            current_position[0] + directions[direction][0],
            current_position[1] + directions[direction][1],
        )

        for position in range(RANGE_SIZE):

            if 0 <= row < RANGE_SIZE and 0 <= col < RANGE_SIZE:

                if shooting_range[row][col] == "x":
                    total_targets_shot += 1
                    shot_targets_positions.append([row, col])
                    shooting_range[row][col] = "."
                    break

            row += directions[direction][0]
            col += directions[direction][1]

    if total_targets_shot == total_targets:
        print(f"Training completed! All {total_targets_shot} targets hit.")
        break
else:
    targets_left = total_targets - total_targets_shot
    print(f"Training not completed! {targets_left} targets left.")

for position in shot_targets_positions:
    print(position)


"""                     Task:
You are participating in a Firearm course. It is a training day at the shooting range.
You will be given a matrix with 5 rows and 5 columns.
It is a shotgun range represented as some symbols separated by a single space:
•	Your position is marked with the symbol "A"
•	Targets marked with symbol "x"
•	All of the empty positions will be marked with "."
After the field state, you will be given an integer representing the number of commands
you will receive. The possible commands are:
•	"move {right/left/up/down} {steps}" - you should move in the given direction with
the given steps. You can only move if the field you want to step on is marked with ".".
•	"shoot {right/left/up/down}" - you should shoot in the given direction
(from your current position without moving). Beware that there might be targets that
stand in the way of other targets, and you cannot reach them - you can shoot only the
nearest target. When you have shot a target, the field becomes empty position (".").
Validate the positions since they can be outside the field.
Keep track of all the shot targets:
•	If at any point there are no targets left, end the program and print:
"Training completed! All {count_targets} targets hit.".
•	If, after you perform all the commands, there are some targets left print:
"Training not completed! {count_left_targets} targets left.".
Finally, print the index positions of the targets that you hit, as shown
in the examples.
Input
•	5 lines representing the field (symbols, separated by a single space)
•	N - count of commands
•	On the following N lines - the commands in the format described above
Output
•	On the first line, print one of the following:
o	If all the targets were shot
"Training completed! All {count_targets} targets hit."
o	Otherwise:
    "Training not completed! {count_left_targets} targets left."
•	Finally, print the index positions "[{row}, {column}]" of the targets that you hit,
as shown in the examples.
Constrains
•	All the commands will be valid
•	There will always be at least one target


Example:
Input:
. . . . .
. . . . .
. A x . .
. . . . .
. x . . .
2
shoot down
shoot right
Output:
Training completed! All 2 targets hit.
[4, 1]
[2, 2]
"""
