matrix_size = int(input())

field_matrix = []
bunny_pos = []

most_egg_direction = ""
most_eggs_path = []
most_eggs = 0

directions = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}

for row in range(matrix_size):
    field_matrix.append(input().split())

    if "B" in field_matrix[row]:
        bunny_pos = row, field_matrix[row].index("B")


for direction, [row, col] in directions.items():
    new_row, new_col = bunny_pos[0] + row, bunny_pos[1] + col

    current_direction_eggs = 0
    current_path = []

    while (
        0 <= new_row < matrix_size
        and 0 <= new_col < matrix_size
        and field_matrix[new_row][new_col] != "X"
    ):
        current_direction_eggs += int(field_matrix[new_row][new_col])
        current_path.append([new_row, new_col])

        new_row += row
        new_col += col

    if current_direction_eggs >= most_eggs:
        most_egg_direction = direction
        most_eggs_path = current_path
        most_eggs = current_direction_eggs


print(most_egg_direction)
print(*most_eggs_path, sep="\n")
print(most_eggs)


# recursion used to solve the problem for training

# matrix_size = int(input())

# field_matrix = []
# bunny_pos = []

# directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

# for row in range(matrix_size):
#     field_matrix.append(input().split())

#     if "B" in field_matrix[row]:
#         bunny_pos = row, field_matrix[row].index("B")


# def choose_best_path(
#     matrix, start_pos, dict, i=0, most_egg_direction="", most_eggs_path=[],most_eggs=0
# ):
#     def movement(
#         matrix, start_row, start_col, step, current_direction_eggs=0, current_path=[]
#     ):
#         row, col = start_row + step[0], start_col + step[1]

#         if (
#             0 <= row < len(matrix[0])
#             and 0 <= col < len(matrix)
#             and matrix[row][col] != "X"
#         ):
#             current_direction_eggs += int(matrix[row][col])
#             current_path.append([row, col])

#             return movement(
#                 matrix, row, col, step, current_direction_eggs, current_path
#             )
#         else:
#             return current_direction_eggs, current_path

#     if i == len(dict):
#         return most_egg_direction, most_eggs_path, most_eggs
#     else:
#         direction, direction_values = list(dict.items())[i]
#         current_direction_eggs, current_path = movement(
#             matrix, start_pos[0], start_pos[1], direction_values
#         )

#         if current_direction_eggs >= most_eggs:
#             most_egg_direction = direction
#             most_eggs_path = current_path
#             most_eggs = current_direction_eggs

#         return choose_best_path(
#             matrix,
#             start_pos,
#             dict,
#             i + 1,
#             most_egg_direction,
#             most_eggs_path,
#             most_eggs,
#         )


# most_egg_direction, most_eggs_path, most_eggs = choose_best_path(
#     field_matrix, bunny_pos, directions
# )

# print(most_egg_direction)
# print(*most_eggs_path, sep="\n")
# print(most_eggs)


"""                     Task:
Your task is to collect as many eggs as possible.
On the first line, you will be given a number representing the size of the field.
On the following few lines, you will be given a field with:
•	One bunny - randomly placed in it and marked with the symbol "B"
•	Number of eggs placed at different positions of the field and traps marked with "X"
Your job is to determine the direction in which the bunny should go to collect the
maximum number of eggs. The directions that should be considered as possible are
up, down, left, and right. If you reach a trap while checking some of the directions,
you should not consider the fields after the trap in this direction.
For more clarifications, see the examples below.
Note: Consider ONLY the paths from which the bunny has collected 1 or more eggs.
Input
•	A number representing the size of the field
•	The matrix representing the field (each position separated by a single space)
Output
•	The direction which should be considered as best (lowercase)
•	The field positions from which we are collecting eggs as lists
•	The total number of eggs collected
Constraints
•	There will NOT be two or more paths consisting of the same total amount of eggs.

Example:
Input:
5
1 3 7 9 11
X 5 4 X 63
7 3 21 95 1
B 1 73 4 9
9 2 33 2 0
Output:
right
[3, 1]
[3, 2]
[3, 3]
[3, 4]
87
"""
