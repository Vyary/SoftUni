number_of_presents = int(input())
neighborhood_size = int(input())

neighborhood_matrix = []
santa_coordinates = []
nice_kids_count = 0
total_nice_kids = 0

directions = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}

for row in range(neighborhood_size):
    neighborhood_matrix.append(input().split())

    if "S" in neighborhood_matrix[row]:
        santa_coordinates = [row, neighborhood_matrix[row].index("S")]

    if "V" in neighborhood_matrix[row]:
        total_nice_kids += neighborhood_matrix[row].count("V")


while number_of_presents != 0:
    direction = input()

    if direction == "Christmas morning":
        break

    move_row, move_col = (
        santa_coordinates[0] + directions[direction][0],
        santa_coordinates[1] + directions[direction][1],
    )
    santa_previous_position = neighborhood_matrix[santa_coordinates[0]][
        santa_coordinates[1]
    ]
    santa_new_position = neighborhood_matrix[move_row][move_col]

    if neighborhood_matrix[move_row][move_col] == "V":
        santa_previous_position = "-"
        santa_new_position = "S"
        santa_coordinates = [move_row, move_col]
        nice_kids_count += 1
        number_of_presents -= 1

    elif neighborhood_matrix[move_row][move_col] == "X":
        santa_previous_position = "-"
        santa_new_position = "S"
        santa_coordinates = [move_row, move_col]

    elif neighborhood_matrix[move_row][move_col] == "C":
        santa_previous_position = "-"
        santa_new_position = "S"
        santa_coordinates = [move_row, move_col]

        for direction_around in directions:

            if number_of_presents > 0:
                around_row, around_col = (
                    santa_coordinates[0] + directions[direction_around][0],
                    santa_coordinates[1] + directions[direction_around][1],
                )

                if neighborhood_matrix[around_row][around_col] == "V":
                    neighborhood_matrix[around_row][around_col] = "-"
                    nice_kids_count += 1
                    number_of_presents -= 1

                elif neighborhood_matrix[around_row][around_col] == "X":
                    neighborhood_matrix[around_row][around_col] = "-"
                    number_of_presents -= 1

    else:
        santa_previous_position = "-"
        santa_new_position = "S"
        santa_coordinates = [move_row, move_col]


if number_of_presents == 0 and nice_kids_count != total_nice_kids:
    print("Santa ran out of presents!")

for row in neighborhood_matrix:
    print(*row)

if nice_kids_count == total_nice_kids:
    print(f"Good job, Santa! {nice_kids_count} happy nice kid/s.")
elif nice_kids_count < total_nice_kids:
    difference = total_nice_kids - nice_kids_count
    print(f"No presents for {difference} nice kid/s.")


"""                     Task:
The presents are ready, and Santa has to deliver them to the kids.
You will receive an integer m for the number of presents Santa has and an integer n for
the size of the neighborhood with a square shape. On the following lines,
you will receive the matrix, which represents the neighborhood.
Santa will be in a random cell, marked with the letter "S". Each cell stands for a
house where children may live. If the cell has "X" on it, that means there lives a
naughty kid. Otherwise, if a nice kid lives there, the cell is marked by "V".
There can also be cells marked with "C" for cookies. All of the empty positions will
be marked with "-".
Santa can move "up", "down", "left", "right" with one position each time. These will
be the commands that you receive. If he moves to a house with a nice kid, the kid
receives a present, but if Santa reaches a house with a naughty kid, he doesn't drop a
present. If the command sends Santa to a cell marked with "C", Santa eats cookies and
becomes happy and extra generous to all the kids around him* (meaning all of them will
receive presents - it doesn't matter if naughty or nice). If Santa has been to a house,
the cell becomes "-".
Note: *around him means on his left, right, upwards, and downwards by one cell. In this
case, Santa doesn't move to these cells, or if he does, he returns to the cell where
the cookie was.
If Santa runs out of presents or receives the command "Christmas morning", you should
end the program.
Keep in mind that you should check whether all the nice kids received presents.
Input
•	On the first line, you are given the integer m - the count of presents
•	On the second - integer n - the size of the neighborhood
•	The following n lines hold the values for every row
•	On each of the following lines you will get a command
Output
•	On the first line:
o	If Santa runs out of presents, but there are still some nice kids left print:
"Santa ran out of presents!"
•	Next, print the matrix.
•	In the end, print one of these messages:
o	If he manages to give all the nice kids presents, print:
"Good job, Santa! {count_nice_kids} happy nice kid/s."
o	Otherwise, print:
"No presents for {count nice kids} nice kid/s."
Constraints
•	The size of the square matrix will be between [2…10].
•	Santa's position will be marked with 'S'.
•	There will always be at least 1 nice kid.
•	There won't be a case where the cookie is on the border of the matrix.

Example:
Input:
3
4
- - - -
V - X -
- V C V
- - - S
left
up
Output:
Santa ran out of presents!
- - - -
V - - -
- - S -
- - - -
No presents for 1 nice kid/s.
"""
