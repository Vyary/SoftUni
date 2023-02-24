rows, cols = map(int, input().split())

blind_man_pos = []
obstacles_pos = []
players_pos = []
touched_players = 0
total_moves = 0

directions = {"up": [-1, 0], "down": [1, 0], "right": [0, 1], "left": [0, -1]}

for row in range(rows):
    current_row = input().split()

    if "B" in current_row:
        blind_man_pos = [row, current_row.index("B")]

    if "O" in current_row:
        for index, element in enumerate(current_row):
            if "O" == element:
                obstacles_pos.append([row, index])

    if "P" in current_row:
        for index, element in enumerate(current_row):
            if "P" == element:
                players_pos.append([row, index])

while True:
    direction = input()

    if direction == "Finish":
        break
    elif touched_players == len(players_pos):
        break

    row, col = (
        blind_man_pos[0] + directions[direction][0],
        blind_man_pos[1] + directions[direction][1],
    )

    if not (0 <= row < rows) or not (0 <= col < cols):
        continue

    if [row, col] in obstacles_pos:
        continue

    if [row, col] in players_pos:
        touched_players += 1
        total_moves += 1
        blind_man_pos = [row, col]
        continue

    total_moves += 1
    blind_man_pos = [row, col]

print("Game over!")
print(f"Touched opponents: {touched_players} Moves made: {total_moves}")
