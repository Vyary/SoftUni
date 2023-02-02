# You are given an array with integers. Write a program to modify the elements after receiving the following commands:
# •	"swap {index1} {index2}" takes two elements and swap their places.
# •	"multiply {index1} {index2}" takes element at the 1st index and multiply it with the element at 2nd index.
# Save the product at the 1st index.
# •	"decrease" decreases all elements in the array with 1.
# Input
# On the first input line, you will be given the initial array values separated by a single space.
# On the next lines you will receive commands until you receive the command "end". The commands are as follow:
# •	"swap {index1} {index2}"
# •	"multiply {index1} {index2}"
# •	"decrease"
# Output
# The output should be printed on the console and consist of elements of the modified array – separated by a comma and
# a single space ", ".

work_list = [int(num) for num in input().split(' ')]


def swap(lst, index_one, index_two):
    work_list[index_one], work_list[index_two] = work_list[index_two], work_list[index_one]
    return lst


def multiply(lst, index_one, index_two):
    lst[index_one] = lst[index_one] * lst[index_two]


while True:
    command = input().split(' ')
    if command[0] == 'end':
        break
    elif command[0] == 'swap':
        index1 = int(command[1])
        index2 = int(command[2])
        swap(work_list, index1, index2)
    elif command[0] == 'multiply':
        index1 = int(command[1])
        index2 = int(command[2])
        multiply(work_list, index1, index2)
    elif command[0] == 'decrease':
        work_list = [num - 1 for num in work_list]

print(*work_list, sep=', ')
