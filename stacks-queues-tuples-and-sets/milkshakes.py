from collections import deque


chocolates_stack = list(map(int, input().split(", ")))
milk_que = deque(map(int, input().split(", ")))

milkshakes_done = 0

while milkshakes_done != 5 and chocolates_stack and milk_que:
    current_chocolate = chocolates_stack.pop()
    current_milk = milk_que.popleft()

    if current_chocolate <= 0 and current_milk <= 0:
        continue
    elif current_chocolate <= 0:
        milk_que.appendleft(current_milk)
        continue
    elif current_milk <= 0:
        chocolates_stack.append(current_chocolate)
        continue

    if current_chocolate == current_milk:
        milkshakes_done += 1
    else:
        milk_que.append(current_milk)
        current_chocolate -= 5
        chocolates_stack.append(current_chocolate)

if milkshakes_done == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates_stack:
    print(f"Chocolate: {', '.join(map(str, chocolates_stack))}")
else:
    print("Chocolate: empty")

if milk_que:
    print(f"Milk: {', '.join(map(str, milk_que))}")
else:
    print("Milk: empty")


"""                     Task:
You are learning how to make milkshakes.
First, you will be given two sequences of integers representing chocolates and
cups of milk.
You have to start from the last chocolate and try to match it with
the first cup of milk.
If their values are equal, you should make a milkshake and remove both ingredients.
Otherwise, you should move the cup of milk at the end of the sequence and decrease the
value of the chocolate by 5 without moving it from its position.
If any of the values are equal to or below 0, you should remove them from the records
right before mixing them with the other ingredient.
When you successfully prepare 5 chocolate milkshakes, or you have no more chocolate or
cups of milk left, you need to stop making chocolate milkshakes.
Input
•	On the first line of input, you will receive the integers representing the
chocolate, separated by  ", ".
•	On the second line of input, you will receive the integers representing the cups of
milk, separated by ", ".
Output
•	On the first line, print:
o	If you successfully made 5 milkshakes:
"Great! You made all the chocolate milkshakes needed!"
o	Otherwise: "Not enough milkshakes."
•	On the second line - print:
o	If there are chocolates left: "Chocolate: {chocolate1}, {chocolate2}, (…)"
o	Otherwise: "Chocolate: empty"
•	On the third line - print:
o	If there are cups of milk left: "Milk: {milk1}, {milk2}, {milk3}, (…)"
o	Otherwise: "Milk: empty"
Constraints
•	All given numbers will be valid integers in the range [-100 … 100].

Example:
Input:
20, 24, -5, 17, 22, 60, 26
26, 60, 22, 17, 24, 10, 55
Output:
Great! You made all the chocolate milkshakes needed!
Chocolate: 20
Milk: 10, 55
"""
