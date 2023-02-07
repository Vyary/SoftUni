symbols = {"-", ",", ".", "!", "?"}

with open("text.txt", "r") as file:
    text = file.readlines()

    for line in text[::2]:
        # rstrip removes all newlines from the end of the string
        current_line = line.rstrip()

        for symbol in symbols:
            current_line = current_line.replace(symbol, "@")

        print(" ".join(current_line.split()[::-1]))


"""                     Task:
Write a program that reads a text file and prints on the console its even lines.
Line numbers start from 0. Before you print the result,
replace {"-", ",", ".", "!", "?"} with "@" and reverse the order of the words.

Example:
text.txt:
-I was quick to judge him, but it wasn't his fault.
-Is this some kind of joke?! Is it?
-Quick, hide here. It is safer.
output.txt:
fault@ his wasn't it but him@ judge to quick was @I
safer@ is It here@ hide @Quick@
"""
