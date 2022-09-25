from math import ceil

height = int(input())
width = int(input())
percent_without_paint = int(input())

painted = False

walls = (height * width) * 4
percentage = walls * (percent_without_paint / 100)
walls_to_paint = ceil(walls - percentage)

action = input()

while action != 'Tired!':
    action = int(action)
    walls_to_paint -= action
    if walls_to_paint <= 0:
        painted = True
        break
    action = input()

if painted:
    if walls_to_paint < 0:
        left = abs(walls_to_paint)
        print(f"All walls are painted and you have {left} l paint left!")
    else:
        print("All walls are painted! Great job, Pesho!")
elif action == 'Tired!':
    print(f"{walls_to_paint} quadratic m left.")
