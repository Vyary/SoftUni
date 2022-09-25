bad_grades_max = int(input())
problem = input()

old_problem = problem
number_of_problems = 0
total_grade = 0
number_of_grades = 0
bad_grades = 0
grades_are_not_sufficient = False

while problem != 'Enough':
    old_problem = problem
    grade = int(input())
    if grade < 5:
        bad_grades += 1
        if bad_grades >= bad_grades_max:
            grades_are_not_sufficient = True
            break
    number_of_problems += 1
    number_of_grades += 1
    total_grade += grade

    problem = input()

if grades_are_not_sufficient:
    print(f"You need a break, {bad_grades} poor grades.")
else:
    average_grades = total_grade / number_of_grades
    print(f"Average score: {average_grades:.2f}")
    print(f"Number of problems: {number_of_problems}")
    print(f"Last problem: {old_problem}")
