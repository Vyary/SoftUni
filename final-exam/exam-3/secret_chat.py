def insert_space(text, index):
    return text[:index] + " " + text[index:]


def reverse(text, substring):
    if substring in text:
        text = text.replace(substring, "", 1)
        return text + substring[::-1]


def change_all(text, find, replace):
    if find in text:
        text = text.replace(find, replace)
    return text


def main():
    concealed_message = input()

    while True:
        operation = input().split(":|:")
        action = operation[0]
        if action == "Reveal":
            break

        subs_index = operation[1]
        if action == "InsertSpace":
            index = int(subs_index)
            concealed_message = insert_space(concealed_message, index)
        elif action == "Reverse":
            if subs_index in concealed_message:
                concealed_message = reverse(concealed_message, subs_index)
            else:
                print("error")
                continue
        elif action == "ChangeAll":
            replacement = operation[2]
            concealed_message = change_all(concealed_message, subs_index, replacement)
        print(concealed_message)
    print(f"You have a new text message: {concealed_message}")


if __name__ == "__main__":
    main()


"""                     Task:
You have plenty of free time, so you decide to write a program that conceals and 
reveals your received messages. Go ahead and type it in!

On the first line of the input, you will receive the concealed message. After that, 
until the "Reveal" command is given, you will receive strings with instructions for 
different operations that need to be performed upon the concealed message 
to interpret it and reveal its actual content. 
There are several types of instructions, split by ":|:"

"InsertSpace:|:{index}":
    Inserts a single space at the given index. The given index will always be valid.
"Reverse:|:{substring}":
    If the message contains the given substring, cut it out, reverse it and add it at 
        the end of the message. 
    If not, print "error".
    This operation should replace only the first occurrence of the given substring if 
        there are two or more occurrences.
"ChangeAll:|:{substring}:|:{replacement}":
    Changes all occurrences of the given substring with the replacement text.
Input / Constraints
    On the first line, you will receive a string with a message.
    On the following lines, you will be receiving commands, split by ":|:".
Output
    After each set of instructions, print the resulting string. 
    After the "Reveal" command is received, print this message:
    "You have a new text message: {message}"
Examples
    Input	                      Output
heVVodar!gniV
ChangeAll:|:V:|:l               hellodar!gnil
Reverse:|:!gnil                 hellodarling!
InsertSpace:|:5                 hello darling!
Reveal                          You have a new text message: hello darling!
"""
