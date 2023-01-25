rows, cols = [int(num) for num in input().split()]

matrix = [[int(num) for num in input().split()] for _ in range(rows)]

biggest_sub_matrix = []
biggest_sub_matrix_sum = float("-inf")

for row in range(rows - 2):
    for col in range(cols - 2):
        current_matrix = [matrix[i + row][col : col + 3] for i in range(3)]

        current_sub_matrix_sum = sum(
            element for current_row in current_matrix for element in current_row
        )

        if current_sub_matrix_sum > biggest_sub_matrix_sum:
            biggest_sub_matrix_sum = current_sub_matrix_sum
            biggest_sub_matrix = current_matrix

print(f"Sum = {biggest_sub_matrix_sum}")
for row in biggest_sub_matrix:
    print(*row, sep=" ")


"""                     Task:
Write a program that reads a rectangular matrix's dimensions and finds the 3x3 square
with a maximum sum of its elements. There will be no case with two or more 3x3 squares
with equal maximal sum.
Input
•	On the first line, you will receive the rows and columns in
the format "{rows} {columns}" - integers in the range [1, 20]
•	On the following lines, you will receive each row with its columns - integers,
separated by a single space in the range [-20, 20]
Output
•	On the first line, print the maximum sum of the elements in
the 3x3 square in the format "Sum = {sum}"
•	On the following 3 lines, print each element of the found sub matrix,
separated by a single space.

Example:
Input:
4 5
1 5 5 2 4
2 1 4 14 3
3 7 11 2 8
4 8 12 16 4
Output:
Sum = 75
1 4 14
7 11 2
8 12 16
"""
