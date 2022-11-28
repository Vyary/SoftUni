stops = input()

while True:
    command = input().split(":")
    if command[0] == "Travel":
        break

    action, arg1, arg2 = command

    if action == "Add Stop":
        index = int(arg1)
        if 0 <= index <= len(stops):
            stops = stops[:index] + arg2 + stops[index:]
    elif action == "Remove Stop":
        start_index = int(arg1)
        end_index = int(arg2)
        if 0 <= start_index < len(stops) and 0 <= end_index < len(stops):
            stops = stops[:start_index] + stops[end_index + 1 :]
    elif action == "Switch":
        if arg1 in stops:
            stops = stops.replace(arg1, arg2)
    print(stops)
print(f"Ready for world tour! Planned stops: {stops}")


"""                     Task:
You are a world traveler, and your next goal is to make a world tour. To do that, 
you have to plan out everything first. To start with, you would like to plan out all 
of your stops where you will have a break.

On the first line, you will be given a string containing all of your stops. 
Until you receive the command "Travel", you will be given some commands to manipulate 
that initial string. The commands can be:
"Add Stop:{index}:{string}":
    Insert the given string at that index only if the index is valid
"Remove Stop:{start_index}:{end_index}":
    Remove the elements of the string from the starting index to the end index 
    (inclusive) if both indices are valid
"Switch:{old_string}:{new_string}":
    If the old string is in the initial string, replace it with the new one 
    (all occurrences)
Note: After each command, print the current state of the string if it is valid!
After the "Travel" command, print the following: 
"Ready for world tour! Planned stops: {string}"
Input / Constraints
    An index is valid if it is between the first and the last element index 
    (inclusive) (0 ….. Nth) in the sequence.
Output
    Print the proper output messages in the proper cases as described in 
    the problem description
Examples
    Input
Hawai::Cyprys-Greece
Add Stop:7:Rome
Remove Stop:11:16
Switch:Hawai:Bulgaria
Travel
    Output
Hawai::RomeCyprys-Greece
Hawai::Rome-Greece
Bulgaria::Rome-Greece
Ready for world tour! Planned stops: Bulgaria::Rome-Greece

"""
