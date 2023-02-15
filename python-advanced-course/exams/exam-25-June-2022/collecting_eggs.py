from collections import deque

BOX_SIZE = 50
total_boxes = 0

egg_sizes = deque(input().split(", "))
pieces_of_paper = input().split(", ")

while egg_sizes and pieces_of_paper:
    current_egg = int(egg_sizes.popleft())
    current_paper = int(pieces_of_paper.pop())

    if current_egg <= 0:
        pieces_of_paper.append(str(current_paper))
        continue
    elif current_egg == 13:
        pieces_of_paper.append(str(current_paper))
        pieces_of_paper[0], pieces_of_paper[-1] = (
            pieces_of_paper[-1],
            pieces_of_paper[0],
        )
        continue

    if current_egg + current_paper <= BOX_SIZE:
        total_boxes += 1

if total_boxes > 0:
    print(f"Great! You filled {total_boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if egg_sizes:
    print(f"Eggs left: {', '.join(egg_sizes)}")
if pieces_of_paper:
    print(f"Pieces of paper left: {', '.join(pieces_of_paper)}")


"""                     Task:
Old MacDonald wants to fill some boxes with eggs. But he has a big farm,
and he will need some help.
On the first line, you will receive a sequence of numbers, each representing an
egg with its size. On the second line, you will receive another sequence of numbers,
each representing a piece of paper with its size.
You should take the first egg and wrap it with the last piece of paper. Then, try to
put it in a box with a size of 50. Each wrapped-in-a-paper egg fills one box if it fits
in it. Your task is to check whether you have filled at least one box.
You should comply with the following conditions:
•	If the egg is not fresh anymore (its size is less than or equal to 0), you need to
remove it from the sequence before it is wrapped with a piece of paper.
•	If the sum of the egg's size and the paper's size is less than or equal to the
box's size (50), put the wrapped egg in the box and remove both from the sequences.
o	Otherwise, you cannot fill a box, so remove both the egg and the paper from the
    sequences without putting them in a box.
•	During your work, you noticed that Old MacDonald is superstitious.
If the size of an egg is 13 it brings bad luck to him. You should remove this egg from
the sequence before it is wrapped with a piece of paper.
o	Furthermore, each time you take an egg with a size of 13,
it will be best to swap the first and last pieces of paper positions to bring the good
luck back to Old MacDonald.
	Note: There will be NO case where there will be just one piece of paper left.
For more clarification see the examples below.
Input
•	In the first line, you will be given a sequence of eggs with their sizes - integers
separated by comma and space ", " in the range [-100, 100]
•	In the second line, you will be given a sequence of pieces of paper with their
sizes - integers separated by comma and space ", " in the range [1, 100]
Output
•	On the first line:
o	If you have at least one box filled, print:
	"Great! You filled {total count} boxes."
o	If you couldn't fill any boxes, print:
	"Sorry! You couldn't fill any boxes!"
•	On the following lines, print the eggs left or pieces of paper left if there are any:
o	Eggs left: {left eggs joined by ", "}
o	Pieces of paper left: {left pieces of paper joined by ", "}

Example:
Input:
20, 13, -7, 7
10, 5, 20, 15, 7, 9
Output:
Great! You filled 2 boxes.
Pieces of paper left: 7, 5, 20, 15
"""