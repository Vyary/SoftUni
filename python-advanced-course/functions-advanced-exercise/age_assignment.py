def age_assignment(*args, **kwargs):
    message = []

    for letter, age in kwargs.items():
        for name in args:
            if name.startswith(letter):
                message.append(f"{name} is {age} years old.")

    return "\n".join(sorted(message))


"""                     Task:
Create a function called age_assignment() that receives a different number of names and
a different number of key-value pairs. The key will be a single letter
(the first letter of each name) and the value - a number (age). Find its first letter
in the key-value pairs for each name and assign the age to the person's name.
Then, sort the names in ascending order (alphabetically) and return the information for
each person on a new line in the format: "{name} is {age} years old."

Example:
Test Code:
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
Output:
Amy is 22 years old.
Bill is 61 years old.
Willy is 36 years old.
"""
