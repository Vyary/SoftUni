# Write a program that finds a place for the tourist on a lift.
# Every wagon should have a maximum of 4 people on it. If a wagon is full, you should direct the people to the next one
# with space available.
# Input
# •	On the first line, you will receive how many people are waiting to get on the lift
# •	On the second line, you will receive the current state of the lift separated by a single space: " ".
# Output
# When there is no more available space left on the lift, or there are no more people in the queue, you should print
# on the console the final state of the lift's wagons separated by " " and one of the following messages:
# •	If there are no more people and the lift have empty spots, you should print:
# "The lift has empty spots!
# {wagons separated by ' '}"
# •	If there are still people in the queue and no more available space, you should print:
# "There isn't enough space! {people} people in a queue!
# {wagons separated by ' '}"
# •	If the lift is full and there are no more people in the queue, you should print only the wagons separated by " "

people = int(input())
lift = [int(num) for num in input().split(' ')]

for wagon in range(len(lift)):
    while lift[wagon] < 4 and people > 0:
        lift[wagon] += 1
        people -= 1

total_lift_size = len(lift) * 4
if people > 0:
    print(f"There isn't enough space! {people} people in a queue!")
elif total_lift_size > sum(lift):
    print("The lift has empty spots!")
print(*lift, sep=' ')
