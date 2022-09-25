end_number = int(input())
current_number = 1

for row in range(1, end_number + 1):
    for length in range(1, row + 1):
        print(current_number, end=' ')
        current_number += 1
        if current_number > end_number:
            break
    if current_number > end_number:
        break
    print()
