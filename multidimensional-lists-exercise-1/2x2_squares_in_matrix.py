rows, cols = [int(num) for num in input().split()]

matrix = [[letter for letter in input().split()] for row in range(rows)]

number_of_identical_squares = 0


for i in range(rows - 1):
    for j in range(cols - 1):
        if (
            matrix[i][j] == matrix[i + 1][j]
            and matrix[i][j] == matrix[i][j + 1]
            and matrix[i][j] == matrix[i + 1][j + 1]
        ):
            number_of_identical_squares += 1

print(number_of_identical_squares)


"""                     Task:
Find the number of all 2x2 squares containing identical chars in a matrix.
On the first line, you will receive the matrix's dimensions in
the format "{rows} {columns}". On the following rows, you will receive characters
separated by a single space. Print the number of all square matrices you have found.

Example:
Input:
3 4
A B B D
E B B B
I J B B
Output:
2
"""
