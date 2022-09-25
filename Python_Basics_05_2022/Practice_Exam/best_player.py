name_of_player = input()

best_player = ''
best_player_goals = 0
player_has_hat_trick = False

while name_of_player != 'END':
    number_of_goals = int(input())
    if number_of_goals > best_player_goals:
        best_player = name_of_player
        best_player_goals = number_of_goals
        if number_of_goals >= 10:
            player_has_hat_trick = True
            break
        elif number_of_goals >= 3:
            player_has_hat_trick = True

    name_of_player = input()

print(f"{best_player} is the best player!")
if player_has_hat_trick:
    print(f"He has scored {best_player_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {best_player_goals} goals.")
