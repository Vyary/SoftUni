from collections import deque

parentheses_que = deque(input())

opening_parentheses_stack = []

while parentheses_que:
    current_parenthesis = parentheses_que.popleft()

    if current_parenthesis in "({[":
        opening_parentheses_stack.append(current_parenthesis)
    elif not opening_parentheses_stack:
        print("NO")
        break
    else:
        if opening_parentheses_stack.pop() + current_parenthesis not in "(){}[]":
            print("NO")
            break
else:
    print("YES")


"""                     Task:
You will be given a sequence consisting of parentheses. Your job is to determine
whether the expression is balanced. A sequence of parentheses is balanced if every
opening parenthesis has a corresponding closing parenthesis that occurs after
the former. There will be no interval symbols between the parentheses.
You will be given three types of parentheses: (), {}, and [].
{[()]} - Parentheses are balanced.
(){}[] - Parentheses are balanced.
{[(])} - Parentheses are NOT balanced.
Input
•	On a single line, you will receive a sequence of parentheses.
Output
•	For each test case, print on a new line "YES" if the parentheses are balanced.
•	Otherwise, print "NO"
Constraints
•	1 ≤ lens ≤ 1000, where the lens is the length of the sequence
•	Each character of the sequence will be one of {, }, (, ), [, ]
Examples
Input:	        Output:
{[()]}	        YES
{[(])}	        NO
{{[[(())]]}}	YES
"""
