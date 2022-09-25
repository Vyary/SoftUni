# Write a program that receives three whole numbers and prints the largest one.

number = 0
num_list = []

for _ in range(3):
    number = int(input())
    num_list.append(number)

print(max(num_list))
