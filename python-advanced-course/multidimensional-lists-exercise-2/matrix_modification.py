matrix_size = int(input())

matrix = []
for _ in range(matrix_size):
    matrix.append([int(num) for num in input().split()])

while True:
    command, *data = input().split()

    if command == "END":
        break

    row, col, value = map(int, data)

    if not 0 <= row < matrix_size or not 0 <= col < matrix_size:
        print("Invalid coordinates")
        continue

    if command == "Add":
        matrix[row][col] += value
    elif command == "Subtract":
        matrix[row][col] -= value

for row in matrix:
    print(*row)


"""                     Task:
Write a program that reads a matrix from the console and changes its values.
On the first line, you will get the matrix's rows - N.
You will get elements for each column on the following N lines,
separated with a single space. You will be receiving commands in the following format:
•	"Add {row} {col} {value}" - Increase the number at the given coordinates with
the value.
•	"Subtract {row} {col} {value}" - Decrease the number at the given coordinates by
the value.
If the coordinate is invalid, you should print "Invalid coordinates". A coordinate is
valid if both of the given indexes are in range [0; len() - 1].
When you receive "END", you should print the matrix and stop the program.

Example:
Input:
3
1 2 3
4 5 6
7 8 9
Add 0 0 5
Subtract 1 1 2
END
Output:
6 2 3
4 3 6
7 8 9
"""
