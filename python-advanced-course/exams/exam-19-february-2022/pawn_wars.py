white_pawn_pos = []
black_pawn_pos = []


def white_pawn_move(current_pos):
    row, col = current_pos
    return row - 1, col


def black_pawn_move(current_pos):
    row, col = current_pos
    return row + 1, col


def white_take_enemy_pawn(current_pos):
    row, col = current_pos

    if (row - 1, col + 1) == black_pawn_pos or (row - 1, col - 1) == black_pawn_pos:
        return True


def black_take_enemy_pawn(current_pos):
    row, col = current_pos

    if (row + 1, col + 1) == white_pawn_pos or (row + 1, col - 1) == white_pawn_pos:
        return True


for row in range(8):
    data = input().split()

    if "w" in data:
        white_pawn_pos = row, data.index("w")

    if "b" in data:
        black_pawn_pos = row, data.index("b")


while True:

    if white_take_enemy_pawn(white_pawn_pos):
        square = f"{chr(97 + black_pawn_pos[1])}{8-black_pawn_pos[0]}"
        print(f"Game over! White win, capture on {square}.")
        break

    white_pawn_pos = white_pawn_move(white_pawn_pos)

    if white_pawn_pos[0] == 0:
        square = f"{chr(97 + white_pawn_pos[1])}{8-white_pawn_pos[0]}"
        print(f"Game over! White pawn is promoted to a queen at {square}.")
        break

    if black_take_enemy_pawn(black_pawn_pos):
        square = f"{chr(97 + white_pawn_pos[1])}{8-white_pawn_pos[0]}"
        print(f"Game over! Black win, capture on {square}.")
        break

    black_pawn_pos = black_pawn_move(black_pawn_pos)

    if black_pawn_pos[0] == 7:
        square = f"{chr(97 + black_pawn_pos[1])}{8-black_pawn_pos[0]}"
        print(f"Game over! Black pawn is promoted to a queen at {square}.")
        break


"""                     Task:
A chessboard has 8 rows and 8 columns. Rows, also called ranks, are marked from
number 1 to 8, and columns are marked from A to H. We have a total of 64 squares.
Each square is represented by a combination of letters and a number (a1, b1, c1, etc.).
In this problem colors of the board will be ignored.
We will play the game with two pawns, white (w) and black (b), where they can:
•	Only move forward in a straight line:
	White (w) moves from the 1st rank to the 8th rank direction.
	Black (b) moves from 8th rank to the 1st rank direction.
•	Can move only 1 square at a time.
•	Can capture another pawn in from of them only diagonally:

When a pawn reaches the last rank (for the white one - this is the 8th rank, and for
the black one - this is the 1st rank), can be promoted to a queen.
Two pawns (w and b) will be placed on two random squares of the board. The first move
is always made by the white pawn (w), then black moves (b), then white (w) again,
and so on.

Some rules apply when moving paws:
•	If the two pawns interact diagonally, the player, in turn, must capture the
opponent's pawn. When a pawn captures another pawn, the game is over.
•	If no capture is possible, the pawns keep on moving until one of them reaches
the last rank.
Input
•	On 8 lines, you will receive each row with its 8 columns, each element separated by
a single space:
o	Empty positions are marked with "-".
o	White pawn is marked with "w"
o	Black pawn is marked with "b"
Output
Print either one of the following:
•	If a pawn captures the other, print:
o	"Game over! {White/Black} win, capture on {square}."
•	If a pawn reaches the last rank, print:
o	"Game over! {White/Black} pawn is promoted to a queen at {square}."

Example:
Input:
- - - - - - - -
- - - - - - - -
- - - - - - - -
- - b - - - - -
- - - - - - - -
- w - - - - - -
- - - - - - - -
- - - - - - - -
Output:
Game over! White pawn is promoted to a queen at b8.
"""
