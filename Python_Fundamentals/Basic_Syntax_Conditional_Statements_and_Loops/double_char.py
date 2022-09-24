# You will be given strings until you receive the command "End". For each string given,
# you should print a string in which each character (case-sensitive) is repeated twice.
# Note that if you receive the string "SoftUni", you should NOT print it!

input_string = input()
doubled_string = ''

while input_string != 'End':
    if input_string != 'SoftUni':
        for letter in input_string:
            doubled_string += letter * 2
        print(doubled_string)
        doubled_string = ''
    input_string = input()
