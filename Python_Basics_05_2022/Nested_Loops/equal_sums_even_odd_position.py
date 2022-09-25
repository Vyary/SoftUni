start_number = int(input())
end_number = int(input())

for number in range(start_number, end_number + 1):
    number = str(number)
    total_of_odds = int(number[1]) + int(number[3]) + int(number[5])
    total_of_evens = int(number[0]) + int(number[2]) + int(number[4])
    if total_of_odds == total_of_evens:
        print(number, end=' ')
