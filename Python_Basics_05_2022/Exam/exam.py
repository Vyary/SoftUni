number_of_students = int(input())

top_students = 0
between_4_and_499 = 0
between_3_and_399 = 0
failed = 0
total = 0


for student in range(number_of_students):
    student_score = float(input())
    total += student_score
    if student_score >= 5:
        top_students += 1
    elif student_score >= 4:
        between_4_and_499 += 1
    elif student_score >= 3:
        between_3_and_399 += 1
    elif student_score < 3:
        failed += 1

top_students_percent = top_students / number_of_students * 100
between_4_and_499_percent = between_4_and_499 / number_of_students * 100
between_3_and_399_percent = between_3_and_399 / number_of_students * 100
failed_percent = failed / number_of_students * 100
average_score = total / number_of_students

print(f'''
Top students: {top_students_percent:.2f}%
Between 4.00 and 4.99: {between_4_and_499_percent:.2f}%
Between 3.00 and 3.99: {between_3_and_399_percent:.2f}%
Fail: {failed_percent:.2f}%
Average: {average_score:.2f}
''')
