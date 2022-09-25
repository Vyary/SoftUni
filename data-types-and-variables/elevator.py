# Calculate how many courses will be needed to elevate N persons by using an elevator with
# a capacity of P persons. The input holds two lines: the number of people N and
# the capacity P of the elevator.

number_of_people = int(input())
elevator_capacity = int(input())

courses = number_of_people // elevator_capacity
if number_of_people % elevator_capacity != 0:
    courses += 1

print(courses)
