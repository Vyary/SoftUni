number_of_numbers = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for number in range(number_of_numbers):
    current_number = int(input())
    if current_number < 200:
        p1 += 1
    elif 200 <= current_number < 400:
        p2 += 1
    elif 400 <= current_number < 600:
        p3 += 1
    elif 600 <= current_number < 800:
        p4 += 1
    elif 800 <= current_number:
        p5 += 1

p1_total = p1 / number_of_numbers * 100
p2_total = p2 / number_of_numbers * 100
p3_total = p3 / number_of_numbers * 100
p4_total = p4 / number_of_numbers * 100
p5_total = p5 / number_of_numbers * 100

print(f'{p1_total:.2f}%')
print(f'{p2_total:.2f}%')
print(f'{p3_total:.2f}%')
print(f'{p4_total:.2f}%')
print(f'{p5_total:.2f}%')
