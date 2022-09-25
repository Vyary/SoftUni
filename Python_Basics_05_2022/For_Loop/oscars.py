name_of_actor = input()
academy_points = float(input())
jury_number = int(input())

for points in range(jury_number):
    jury_name = len(input())
    jury_points = float(input())

    jury_score = (jury_name * jury_points) / 2
    academy_points += jury_score

    if academy_points > 1250.5:
        break

if academy_points < 1250.5:
    diff = abs(academy_points - 1250.5)
    print(f"Sorry, {name_of_actor} you need {diff:.1f} more!")
else:
    print(f"Congratulations, {name_of_actor} got a nominee for leading role with {academy_points:.1f}!")
