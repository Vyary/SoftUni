deposit_amount = float(input())
months_of_deposit = int(input())
annual_percentage = float(input())

annual_percentage_in_percents = annual_percentage / 100
interest_rate_per_year = deposit_amount * annual_percentage_in_percents
interest_rate_per_month = interest_rate_per_year / 12

total_sum_with_interest_rate = deposit_amount + months_of_deposit * interest_rate_per_month
print(total_sum_with_interest_rate)
