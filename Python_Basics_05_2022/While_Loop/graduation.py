name_of_student = input()
current_class = 1
total_grades = 0
bad_grades = 0
is_excluded = False

while current_class <= 12:
    new_grade = float(input())

    if new_grade >= 4:
        current_class += 1
        total_grades += new_grade
        continue

    bad_grades += 1
    if bad_grades > 1:
        is_excluded = True
        break

if is_excluded:
    print(f"{name_of_student} has been excluded at {current_class} grade")
else:
    average_grade = total_grades / 12
    print(f"{name_of_student} graduated. Average grade: {average_grade:.2f}")
