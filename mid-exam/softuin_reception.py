# Three employees are working on the reception all day. Each of them can handle a different number of students per hour.
# Your task is to calculate how much time it will take to answer all the questions of a given number of students.
# First, you will receive 3 lines with integers,
# representing the number of students that each employee can help per hour.
# On the following line, you will receive students count as a single integer.
# Every fourth hour, all employees have a break, so they don't work for an hour. It is the only break for the employees,
# because they don't need rest, nor have a personal life.
# Calculate the time needed to answer all the student's questions
# and print it in the following format: "Time needed: {time}h."
# Input / Constraints
# •	On the first three lines -  each employee efficiency -  integer in the range [1 - 100]
# •	On the fourth line - students count – integer in the range [0 – 10000]
# •	Input will always be valid and in the range specified
# Output
# •	Print a single line: "Time needed: {time}h."

employee_one = int(input())
employee_two = int(input())
employee_three = int(input())
students = int(input())

total_employee_efficiency = employee_one + employee_two + employee_three
total_hours = 0

while students > 0:
    students -= total_employee_efficiency
    total_hours += 1
    if total_hours % 4 == 0 and total_hours != 0:
        students += total_employee_efficiency

print(f"Time needed: {total_hours}h.")
