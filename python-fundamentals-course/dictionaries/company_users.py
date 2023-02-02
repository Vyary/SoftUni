# Write a program that keeps the information about companies and their employees.
# You will be receiving company names and an employees' id until you receive the command "End" command.
# Add each employee to the given company. Keep in mind that a company cannot have two employees with the same id.
# Print the company name and each employee's id in the following format:
# "{company_name}
# -- {id1}
# -- {id2}
# …
# -- {idN}"

company_employee_dict = {}

while True:
    entry = input().split(' -> ')
    if entry[0] == 'End':
        break
    company = entry[0]
    employee = entry[1]
    if company not in company_employee_dict:
        company_employee_dict[company] = []
    if employee not in company_employee_dict[company]:
        company_employee_dict[company].append(employee)

for company in company_employee_dict:
    print(company)
    for employee in company_employee_dict[company]:
        print(f'-- {employee}')
