def take_odd(text):
    return "".join(text[1::2])


def cut(text, index, length):
    substring = text[index : index + length]
    return text.replace(substring, "", 1)


def substitute(text, find, replace):
    if find in text:
        return text.replace(find, replace)
    return text


def main():
    raw_password = input()
    while True:
        command = input().split()
        if command[0] == "Done":
            break
        elif command[0] == "TakeOdd":
            raw_password = take_odd(raw_password)
            print(raw_password)
        elif command[0] == "Cut":
            start_index = int(command[1])
            cut_length = int(command[2])
            raw_password = cut(raw_password, start_index, cut_length)
            print(raw_password)
        elif command[0] == "Substitute":
            substring = command[1]
            substitute_text = command[2]
            if substring in raw_password:
                raw_password = substitute(raw_password, substring, substitute_text)
                print(raw_password)
            else:
                print("Nothing to replace!")

    print(f"Your password is: {raw_password}")


if __name__ == "__main__":
    main()


"""                     Task:
Yet again, you have forgotten your password. Naturally, it's not the first time this 
has happened. Actually, you got so tired of it that you decided to help yourself with 
an intelligent solution.

Write a password reset program that performs a series of commands upon a predefined 
string. First, you will receive a string, and afterward, until the command "Done" is 
given, you will be receiving strings with commands split by a single space. 
The commands will be the following:

"TakeOdd"
    Takes only the characters at odd indices and concatenates them to obtain the new 
        raw password and then prints it.
"Cut {index} {length}"
    Gets the substring with the given length starting from the given index from the 
        password and removes its first occurrence, 
        then prints the password on the console.
    The given index and the length will always be valid.
"Substitute {substring} {substitute}"
    If the raw password contains the given substring, replaces all of its 
        occurrences with the substitute text given and prints the result.
Input
    You will be receiving strings until the "Done" command is given.
Output
    After the "Done" command is received, print: "Your password is: {password}"
Constraints
    The indexes from the "Cut {index} {length}" command will always be valid.
Examples
                Input                                   Output
Siiceercaroetavm!:?:ahsott.:i:nstupmomceqr          
TakeOdd                                             icecream::hot::summer
Cut 15 3                                            icecream-hot-mer
Substitute :: -                                     icecream-hot-mer
Substitute | ^                                      Nothing to replace!
Done                                                Your password is: icecream-hot-mer
"""
