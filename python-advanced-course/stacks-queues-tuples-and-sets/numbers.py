def add_numbers_to_set(set_name, numbers):

    for number in numbers:
        set_name.add(number)


def remove_numbers_from_set(set_name, numbers):

    for number in numbers:
        set_name.discard(number)


def list_of_numbers_from_input(text):
    numbers_list = [int(num) for num in command.split() if num.isdigit()]

    return numbers_list


first_set = set(int(num) for num in input().split())
second_set = set(int(num) for num in input().split())

for _ in range(int(input())):
    command = input()
    numbers = list_of_numbers_from_input(command)

    if command.startswith("Add First"):
        add_numbers_to_set(first_set, numbers)
    elif command.startswith("Add Second"):
        add_numbers_to_set(second_set, numbers)
    elif command.startswith("Remove First"):
        remove_numbers_from_set(first_set, numbers)
    elif command.startswith("Remove Second"):
        remove_numbers_from_set(second_set, numbers)
    elif command.startswith("Check Subset"):
        if first_set.issubset(second_set) or second_set.issubset(first_set):
            print("True")
        else:
            print("False")

print(*(sorted(first_set)), sep=", ")
print(*(sorted(second_set)), sep=", ")


"""                     Task:
First, you will be given two sequences of integers values on different lines.
The values of the sequences are separated by a single space between them.
Keep in mind that each sequence should contain only unique values.
Next, you will receive a number - N. On the next N lines, you will receive one of
the following commands:
•	"Add First {numbers, separated by a space}" -add the given numbers at the end of
the first sequence of numbers.
•	"Add Second {numbers, separated by a space}" - add the given numbers at the end of
the second sequence of numbers.
•	"Remove First {numbers, separated by a space}" - remove only the numbers contained
in the first sequence.
•	"Remove Second {numbers, separated by a space}" - remove only the numbers contained
in the second sequence.
•	"Check Subset" - check if any of the given sequences are a subset of the other.
If it is, print "True". Otherwise, print "False".
In the end, print the final sequences, separated by a comma and a space ", ".
The values in each sequence should be sorted in ascending order.

Example:
Input:
1 2 3 4 5
1 2 3
3
Add First 5 6
Remove Second 8 9 11
Check Subset
Output:
True
1, 2, 3, 4, 5, 6
1, 2, 3
"""
