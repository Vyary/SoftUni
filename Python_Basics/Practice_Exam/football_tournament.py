name_of_team = input()
number_of_matches = int(input())

total_w = 0
total_d = 0
total_l = 0
total_points = 0

for match in range(number_of_matches):
    match_result = input()
    if match_result == 'W':
        total_w += 1
        total_points += 3
    elif match_result == 'D':
        total_d += 1
        total_points += 1
    elif match_result == 'L':
        total_l += 1

if number_of_matches == 0:
    print(f"{name_of_team} hasn't played any games during this season.")
else:
    print(f"{name_of_team} has won {total_points} points during this season.")
    print(f"Total stats:")
    print(f"## W: {total_w}")
    print(f"## D: {total_d}")
    print(f"## L: {total_l}")
    percent_wins = (total_w / number_of_matches) * 100
    print(f"Win rate: {percent_wins:.2f}%")
