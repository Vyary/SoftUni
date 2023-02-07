from string import punctuation

with open("text.txt", "r") as file:
    text = file.readlines()

    with open("output.txt", "w") as outfile:

        for line_num, line in enumerate(text):
            line = line.rstrip()

            letter_count = sum(1 for char in line if char.isalpha())
            symbol_count = sum(1 for char in line if char in punctuation)

            outfile.write(
                f"Line {line_num + 1}: {line} ({letter_count})({symbol_count})\n"
            )


"""                     Task:
Write a program that reads a text file, inserts line numbers in front of each line,
and counts all the letters and punctuation marks. The result should be written to
another text file.

Example:
text.txt:
-I was quick to judge him, but it wasn't his fault.
-Is this some kind of joke?! Is it?
-Quick, hide here. It is safer.
output.txt:
Line 1: -I was quick to judge him, but it wasn't his fault. (37)(4)
Line 2: -Is this some kind of joke?! Is it? (24)(4)
Line 3: -Quick, hide here. It is safer. (22)(4)
"""
