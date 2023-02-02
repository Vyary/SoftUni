# You are a facility manager at a large business center.
# One of your responsibilities is to check if each conference room in the center has enough chairs for the visitors.
# On the first line, you will be given an integer n representing the number of rooms in the business center.
# On the following n lines for each room, you will receive information about the chairs in the room and
# the number of visitors. Each chair will be presented with the char "X".
# Next, there will be a single space and the number of visitors at the end.
# For example: "XXXXX 4" (5 chairs and 4 visitors).
# Keep track of the free chairs:
# •	If there are not enough chairs in a specific room,
# print the following message: "{needed_chairs_in_room} more chairs needed in room {number_of_room}".
# The rooms start from 1.
# •	Otherwise, print: "Game On, {total_free_chairs} free chairs left".

rooms = int(input())
total_free_chairs = 0
enough_space = True

for room in range(1, rooms + 1):
    chairs_and_visitors = input().split(' ')
    chairs = len(chairs_and_visitors[0])
    visitors = int(chairs_and_visitors[1])
    diff = abs(visitors - chairs)
    if visitors > chairs:
        print(f"{diff} more chairs needed in room {room}")
        enough_space = False
    else:
        total_free_chairs += diff

if enough_space:
    print(f"Game On, {total_free_chairs} free chairs left")
