number = int(input())

for x1 in range(1, 10):
    for x2 in range(1, 10):
        for x3 in range(1, 10):
            for x4 in range(1, 10):
                if number % x1 == 0 and number % x2 == 0 and number % x3 == 0 and number % x4 == 0:
                    print(f"{x1}{x2}{x3}{x4}", end=' ')
