name_of_company = input()
adult_tickets = int(input())
kids_tickets = int(input())
adult_ticket_price = float(input())
additional_costs = float(input())

kids_ticket_price = adult_ticket_price * 0.30 + additional_costs
adult_ticket_price = adult_ticket_price + additional_costs

adult_total = adult_tickets * adult_ticket_price
kids_total = kids_tickets * kids_ticket_price

sum_total = adult_total + kids_total
profit = sum_total * 0.20

print(f"The profit of your agency from {name_of_company} tickets is {profit:.2f} lv.")
