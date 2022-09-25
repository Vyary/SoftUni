width = int(input())
length = int(input())
height = int(input())

total_space = width * length * height

while total_space >= 0:
    new_taken_space = input()
    if new_taken_space == 'Done':
        break
    new_taken_space = int(new_taken_space)
    total_space -= new_taken_space

if total_space < 0:
    print(f"No more free space! You need {abs(total_space)} Cubic meters more.")
else:
    print(f"{total_space} Cubic meters left.")
