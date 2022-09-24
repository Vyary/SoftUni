# Help out the sorting hat to sort the new students in the houses of Hogwarts.
# You will be receiving names until the student_name "Welcome!". The length of each name
# determines in which house the student is going:
# •	If the name is less than 5 chars, the student is going into Gryffindor
# o	Print "{name} goes to Gryffindor."
# •	If the name is exactly 5 chars, the student is going into Slytherin
# o	Print "{name} goes to Slytherin."
# •	If the name is exactly 6 chars, the student is going into Ravenclaw
# o	Print "{name} goes to Ravenclaw."
# •	If the name is more than 6 chars, the student is going into Hufflepuff
# o	Print "{name} goes to Hufflepuff."
# While receiving names, if you receive "Voldemort", print "You must not speak of that name!" and
# end the program. No more sorting for today!
# If all students are sorted successfully, print "Welcome to Hogwarts."

student_name = input()
no_more_sorting = False

while student_name != 'Welcome!':
    if len(student_name) < 5:
        print(f"{student_name} goes to Gryffindor.")
    elif len(student_name) == 5:
        print(f"{student_name} goes to Slytherin.")
    elif len(student_name) == 6:
        print(f"{student_name} goes to Ravenclaw.")
    elif len(student_name) > 6 and student_name != 'Voldemort':
        print(f"{student_name} goes to Hufflepuff.")
    if student_name == 'Voldemort':
        print('You must not speak of that name!')
        no_more_sorting = True
        break
    student_name = input()

if not no_more_sorting:
    print("Welcome to Hogwarts.")
