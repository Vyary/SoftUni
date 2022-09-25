number_of_tabs = int(input())
salary = int(input())

for i in range(number_of_tabs):
    tab_title = input()

    if tab_title == 'Facebook':
        salary -= 150
    elif tab_title == 'Instagram':
        salary -= 100
    elif tab_title == 'Reddit':
        salary -= 50

    if salary <= 0:
        break

if salary <= 0:
    print("You have lost your salary.")
else:
    print(salary)
