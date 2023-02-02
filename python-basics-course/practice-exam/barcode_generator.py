start_number = int(input())
end_number = int(input())

start_number_str = str(start_number)
end_number_str = str(end_number)

for n1 in range(int(start_number_str[0]), int(end_number_str[0]) + 1):
    for n2 in range(int(start_number_str[1]), int(end_number_str[1]) + 1):
        for n3 in range(int(start_number_str[2]), int(end_number_str[2]) + 1):
            for n4 in range(int(start_number_str[3]), int(end_number_str[3]) + 1):
                if n1 % 2 != 0 and n2 % 2 != 0 and n3 % 2 != 0 and n4 % 2 != 0:
                    print(f'{n1}{n2}{n3}{n4}', end=' ')
