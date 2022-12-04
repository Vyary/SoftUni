def change(text, find, replace):
    text = text.replace(find, replace)
    return text


def includes(text, substring):
    if substring in text:
        return True
    return False


def ends_with(text, substring):
    if text.endswith(substring):
        return True
    return False


def uppercase(text):
    return text.upper()


def find_char(text, char):
    return text.index(char)


def cut(text, start, end):
    return text[start:end]


def main():
    text = input()
    while True:
        command = input().split()
        if command[0] == "Done":
            break
        elif command[0] == "Change":
            find = command[1]
            replace = command[2]
            text = change(text, find, replace)
            print(text)
        elif command[0] == "Includes":
            substring = command[1]
            print(includes(text, substring))
        elif command[0] == "End":
            substring = command[1]
            print(ends_with(text, substring))
        elif command[0] == "Uppercase":
            text = uppercase(text)
            print(text)
        elif command[0] == "FindIndex":
            char = command[1]
            print(find_char(text, char))
        elif command[0] == "Cut":
            start_index = int(command[1])
            end_index = start_index + int(command[2])
            text = cut(text, start_index, end_index)
            print(text)


if __name__ == "__main__":
    main()
