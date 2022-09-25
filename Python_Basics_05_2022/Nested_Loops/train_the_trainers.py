jury = int(input())
presentation = input()
overall_total = 0
scores_total = 0

while presentation != 'Finish':
    presentation_total = 0
    for scores in range(jury):
        score = float(input())
        presentation_total += score
        overall_total += score
        scores_total += 1

    presentation_average = presentation_total / jury
    print(f"{presentation} - {presentation_average:.2f}.")
    presentation = input()

overall_average = overall_total / scores_total
print(f"Student's final assessment is {overall_average:.2f}.")
