from datetime import datetime, timedelta
from collections import deque

robots_data = input().split(";")
starting_time = input()
total_time = datetime.strptime(starting_time, "%H:%M:%S")

robots_dictionary = {}
products_que = deque([])

for robot in robots_data:
    name, process_time = robot.split("-")
    robots_dictionary[name] = {}
    robots_dictionary[name]["name"] = name
    robots_dictionary[name]["process_time"] = int(process_time)
    robots_dictionary[name]["job_time_left"] = robots_dictionary[name]["process_time"]
    robots_dictionary[name]["busy"] = False

while True:
    command = input()
    if command == "End":
        break
    products_que.append(command)
    while products_que:
        total_time += timedelta(seconds=1)

        for robot in robots_dictionary:
            if robots_dictionary[robot]["busy"] is False:
                robots_dictionary[robot]["busy"] = True
                product = products_que.popleft()
                print(
                    f"{robots_dictionary[robot]['name']} - {product} [{total_time:%H:%M:%S}]"
                )
            if robots_dictionary[robot]["busy"] is True:
                robots_dictionary[robot]["job_time_left"] -= 1
                if robots_dictionary[robot]["job_time_left"] == 0:
                    robots_dictionary[robot]["busy"] = False
                    robots_dictionary[robot]["job_time_left"] = robots_dictionary[
                        robot
                    ]["process_time"]
    products_que.rotate(-1)
