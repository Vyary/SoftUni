import os


def create_file(filename):
    with open(filename, "w") as file:
        file.write("")


def add_to_file(filename, text):
    with open(filename, "a") as file:
        file.write(text + "\n")


def replace_in_file(filename, find, replace):
    if not os.path.exists(filename):
        print("An error occurred")
        return

    with open(filename, "r+") as file:
        content = file.read()

        content = content.replace(find, replace)
        # seek moves the file pointer to the beginning
        file.seek(0)
        file.write(content)
        # truncate removes empty lines at the bottom
        file.truncate()


def delete_file(filename):
    if not os.path.exists(filename):
        print("An error occurred")
        return

    os.remove(filename)


commands = {
    "Create": create_file,
    "Add": add_to_file,
    "Replace": replace_in_file,
    "Delete": delete_file,
}

while True:
    line = input().strip()
    if line == "End":
        break

    command, *data = line.split("-")
    commands[command](*data)


"""                     Task:
Create a program that will receive commands until the command "End".
The commands can be:
•	"Create-{file_name}" - Creates the given file with an empty content.
If the file already exists, remove the existing text in it
(as if the file is created again)
•	"Add-{file_name}-{content}" - Append the content and a new line after it.
If the file does not exist, create it, and add the content
•	"Replace-{file_name}-{old_string}-{new_string}" - Open the file and replace all the
occurrences of the old string with the new string. If the file does not exist, print:
"An error occurred"
•	"Delete-{file_name}" - Delete the file. If the file does not exist, print:
"An error occurred"

Example:
Input:
Create-file.txt
Add-file.txt-First Line
Add-file.txt-Second Line
Replace-random.txt-Some-some
Replace-file.txt-First-1st
Replace-file.txt-Second-2nd
Delete-random.txt
Delete-file.txt
End
Comment:
The first command creates the empty file
After the first and second Add command, the content is:
First Line
Second Line
On the first Replace command, an error must occur
After the next two Replace commands, the content is:
1st Line
2nd Line
After the first Delete command, an error occurs
Finally, the 'file.txt' file is deleted
"""
