from math import ceil

name_of_series = input()
episode_length = int(input())
rest_time = int(input())

lunch_break = rest_time / 8
rest = rest_time / 4

rest_time_left = rest_time - (lunch_break + rest)
difference = ceil(abs(rest_time - (lunch_break + rest + episode_length)))

if rest_time_left >= episode_length:
    print(f"You have enough time to watch {name_of_series} and left with {difference} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_of_series}, you need {difference} more minutes.")
