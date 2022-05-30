hour_of_exam = int(input())
minutes_of_exam = int(input())
hour_of_arrival = int(input())
minutes_of_arrival = int(input())

exam_time = hour_of_exam * 60 + minutes_of_exam
arrival_time = hour_of_arrival * 60 + minutes_of_arrival
diff = abs(exam_time - arrival_time)
hours = diff // 60
minutes = diff % 60

late = False
on_time = False
early = False

if arrival_time > exam_time:
    late = True
elif diff <= 30:
    on_time = True
elif diff > 30:
    early = True

if late:
    print('Late')
    if hours > 0:
        print(f'{hours}:{minutes:02d} hours after the start')
    else:
        print(f"{minutes} minutes after the start")
if on_time:
    print('On time')
    if diff >= 1:
        print(f'{minutes} minutes before the start')
if early:
    print('Early')
    if hours > 0:
        print(f'{hours}:{minutes:02d} hours before the start')
    else:
        print(f'{diff} minutes before the start')
