annual_price = int(input())

basketball_shoes = annual_price * 0.6
basketball_clothes = basketball_shoes * 0.8
basketball_ball = basketball_clothes / 4
basketball_accessories = basketball_ball / 5

total_sum = annual_price + basketball_shoes + basketball_clothes + basketball_ball + basketball_accessories

print(total_sum)
