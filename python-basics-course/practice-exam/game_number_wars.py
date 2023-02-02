name_of_player_one = input()
name_of_player_two = input()

player_one_points = 0
player_two_points = 0
number_wars = False
player_one_wins = False
player_two_wins = False

card_of_player_one = int(input())
while card_of_player_one != "End of game":
    card_of_player_one = int(card_of_player_one)
    card_of_player_two = int(input())
    if card_of_player_one > card_of_player_two:
        if number_wars:
            player_one_wins = True
            break
        player_one_points += card_of_player_one - card_of_player_two
    elif card_of_player_two > card_of_player_one:
        if number_wars:
            player_one_wins = True
            break
        player_two_points += card_of_player_two - card_of_player_one
    else:
        number_wars = True

    card_of_player_one = input()

if number_wars:
    print("Number wars!")
    if player_one_wins:
        print(f"{name_of_player_one} is winner with {player_one_points} points")
    elif player_two_wins:
        print(f"{name_of_player_two} is winner with {player_two_points} points")
else:
    print(f"{name_of_player_one} has {player_one_points} points")
    print(f"{name_of_player_two} has {player_two_points} points")
