rows = int(input())

matrix = [[int(num) for num in input().split()] for row in range(rows)]

primary = 0
secondary = 0

for i in range(0, rows):
    primary += matrix[i][i]
    secondary += matrix[i][rows - i - 1]

print(f"{abs(primary - secondary)}")


"""                     Task:
Write a program that finds the difference between the sums of
the square matrix diagonals (absolute value).
On the first line, you will receive an integer N - the size of a square matrix.
The following N lines hold the values for each column - N numbers separated by
a single space.
Print the absolute difference between the primary and the secondary diagonal sums.

Example:
Input:
3
11 2 4
4 5 6
10 8 -12
Output:
15
"""
