from functools import reduce
import re

text = input()
emoji_pattern = r"(:{2}|\*{2})([A-Z][a-z]{2,})\1"
all_emojis = re.findall(emoji_pattern, text)
all_digits = re.findall(r"\d", text)
threshold = int(reduce(lambda x, y: int(x) * int(y), all_digits))
cool_emojis = []

for emoji in all_emojis:
    total_coolness = sum([ord(letter) for letter in emoji[1]])
    if total_coolness >= threshold:
        cool_emojis.append(emoji[0] + emoji[1] + emoji[0])

print(f"Cool threshold: {threshold}")
print(f"{len(all_emojis)} emojis found in the text. The cool ones are:")
print("\n".join(cool_emojis))


"""                     Task:
Your task is to write a program that extracts emojis from a 
text and find the threshold based on the input.
You have to get your cool threshold. It is obtained by 
multiplying all the digits found in the input.  
The cool threshold could be a huge number, so be mindful.
An emoji is valid when:
    It is surrounded by 2 characters, either "::" or "**"
    It is at least 3 characters long (without the surrounding symbols)
    It starts with a capital letter
    Continues with lowercase letters only
    
Examples of valid emojis: ::Joy::, **Banana**, ::Wink::
Examples of invalid emojis: ::Joy**, ::fox:es:, **Monk3ys**, :Snak::Es::

You need to count all valid emojis in the text and calculate their coolness. 
The coolness of the emoji is determined by summing all the ASCII values 
of all letters in the emoji. 
Examples: ::Joy:: - 306, **Banana** - 577, ::Wink:: - 409

You need to print the result of the cool threshold and, after that to take all 
emojis out of the text, count them and print only the cool ones on the console.

Input
    On the single input, you will receive a piece of string. 
Output
    On the first line of the output, 
    print the obtained Cool threshold in the format:
"Cool threshold: {coolThresholdSum}"
    On the following line, 
    print the count of all emojis found in the text in format:
    "{countOfAllEmojis} emojis found in the text. The cool ones are:
    {cool emoji 1}
    {cool emoji 2}
    …
    {cool emoji N}"
Examples
            Input                               Output
    In the Sofia Zoo there are 311          Cool threshold: 540
    animals in total! ::Smiley:: This       4 emojis found in the text. 
    includes 3 **Tigers**, 1 ::Elephant:,   The cool ones are:
    12 **Monk3ys**, a **Gorilla::,          ::Smiley:: 
    5 ::fox:es: and 21 different types of   **Tigers** 
    :Snak::Es::. ::Mooning:: **Shy**        ::Mooning::
"""
