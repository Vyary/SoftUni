movie = input()

student_count_total = 0
standard_count_total = 0
kids_count_total = 0
total_movie = 0
total_tickets = 0
percent_students = 0
percent_standard = 0
percent_kids = 0

while movie != "Finish" and movie != "End":
    seats = int(input())
    free_seats = seats
    while free_seats != 0:
        ticket_type = input()
        if ticket_type == 'student':
            free_seats -= 1
            student_count_total += 1
            total_movie += 1
            total_tickets += 1
        elif ticket_type == 'standard':
            free_seats -= 1
            standard_count_total += 1
            total_movie += 1
            total_tickets += 1
        elif ticket_type == 'kid':
            free_seats -= 1
            kids_count_total += 1
            total_movie += 1
            total_tickets += 1
        else:
            break

    theater_capacity = (total_movie / seats) * 100
    print(f"{movie} - {theater_capacity:.2f}% full.")
    total_movie = 0

    movie = input()

if total_tickets > 0:
    percent_students = (student_count_total / total_tickets) * 100
    percent_standard = (standard_count_total / total_tickets) * 100
    percent_kids = (kids_count_total / total_tickets) * 100

print(f"Total tickets: {total_tickets}")
print(f"{percent_students:.2f}% student tickets.")
print(f"{percent_standard:.2f}% standard tickets.")
print(f"{percent_kids:.2f}% kids tickets.")
