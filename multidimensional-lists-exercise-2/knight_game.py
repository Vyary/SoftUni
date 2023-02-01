matrix_size = int(input())

chess_matrix = []

strongest_knight_power = 0
strongest_knight_pos = []
knights_removed = 0

for _ in range(matrix_size):
    chess_matrix.append(list(input()))

moves = (
    # (row, col)
    (-2, -1),  # top, top, left
    (-2, 1),  # top, top, right
    (2, -1),  # bottom, bottom, left
    (2, 1),  # bottom, bottom, right
    (-1, 2),  # right, right, top
    (1, 2),  # right, right, top
    (-1, -2),  # left, left, top
    (1, -2),  # left, left, bottom
)


while True:

    for row in range(matrix_size):
        for col in range(matrix_size):

            if chess_matrix[row][col] == "K":
                current_knight_power = 0

                for move in moves:
                    possible_row = row + move[0]
                    possible_col = col + move[1]

                    if (
                        0 <= possible_row < matrix_size
                        and 0 <= possible_col < matrix_size
                    ):
                        if chess_matrix[possible_row][possible_col] == "K":
                            current_knight_power += 1

                            if current_knight_power > strongest_knight_power:
                                strongest_knight_power = current_knight_power
                                strongest_knight_pos = row, col

    if strongest_knight_pos:
        knight_row, knight_col = strongest_knight_pos

        chess_matrix[knight_row][knight_col] = "0"
        knights_removed += 1

        strongest_knight_power = 0
        strongest_knight_pos = []
    else:
        break

print(knights_removed)


"""                     Task:
Chess is the oldest game, but it is still popular these days.
It will be used only one chess piece for this task - the Knight.
A chess knight has 8 possible moves it can make, as illustrated.
It can move to the nearest square but not on the same row, column,
or diagonal. (e.g., it can move two squares horizontally, then one square vertically,
or it can move one square horizontally then two
squares vertically - i.e., in an "L" pattern.)
The knight game is played on a board with dimensions N x N.
You will receive a board with "K" for knights and "0" for empty cells. Your task is to
remove knights until no knights that can attack one another with one move are left.
Always remove the knight who can attack the greatest number of knights. If there are
two or more knights with the same number of attacks, remove the top-left one.
Input
•	On the first line, you will receive integer N - the size of the board
•	On the following N lines, you will receive strings with "K" and "0"
Output
•	Print a single integer with the number of knights that need to be removed.

Example:
Input:
5
0K0K0
K000K
00K00
K000K
0K0K0
Output:
1
"""
