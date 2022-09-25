number = int(input())

number_str = str(number)

for n1 in range(1, int(number_str[2]) + 1):
    for n2 in range(1, int(number_str[1]) + 1):
        for n3 in range(1, int(number_str[0]) + 1):
            total = n1 * n2 * n3
            print(f"{n1} * {n2} * {n3} = {total};")
