rows, cols = [int(num) for num in input().split()]

matrix = [input().split(" ") for _ in range(rows)]

while True:
    command, *data = input().split()
    if command == "END":
        break

    if command != "swap" or len(data) != 4:
        print("Invalid input!")
        continue

    row_1, col_1, row_2, col_2 = [int(num) for num in data if num.isdigit()]

    if (
        row_1 in range(rows)
        and row_1 >= 0
        and row_2 in range(rows)
        and row_2 >= 0
        and col_1 in range(cols)
        and col_1 >= 0
        and col_2 in range(cols)
        and col_2 >= 0
    ):
        matrix[row_1][col_1], matrix[row_2][col_2] = (
            matrix[row_2][col_2],
            matrix[row_1][col_1],
        )

        for row in matrix:
            print(*row, sep=" ")
    else:
        print("Invalid input!")


"""                     Task:
Write a program that reads a matrix from the console and performs certain operations
with its elements. User input is provided similarly to the problems above - first,
you read the dimensions and then the data.
Your program should receive commands in the format: "swap {row1} {col1} {row2} {col2}"
where ("row1", "col1") and ("row2", "col2") are the coordinates of
two points in the matrix.
A valid command starts with the "swap" keyword along with four valid coordinates
(no more, no less), separated by a single space.
•	If the command is valid, you should swap the values at the given indexes and
print the matrix at each step (thus, you will be able to check if the operation was
performed correctly).
•	If the command is not valid (does not contain the keyword "swap", has fewer or
more coordinates entered, or the given coordinates are not valid),
print "Invalid input!" and move on to the following command.
A negative value makes the coordinates not valid.
Your program should finish when the command "END" is entered.

Example:
Input:
2 3
1 2 3
4 5 6
swap 0 0 1 1
swap 10 9 8 7
swap 0 1 1 0
END
Output:
5 2 3
4 1 6
Invalid input!
5 4 3
2 1 6
"""
