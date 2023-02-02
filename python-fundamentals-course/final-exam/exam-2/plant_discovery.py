number_of_plants = int(input())
plants = {}

for _ in range(number_of_plants):
    new_plant = input().split("<->")
    plants[new_plant[0]] = {"rarity": new_plant[1], "rating": []}

while True:
    command = input().split(" ")
    if command[0] == "Exhibition":
        break

    action = command[0]
    plant = command[1]
    if plant in plants:
        if action == "Rate:":
            rating = int(command[3])
            plants[plant]["rating"].append(rating)
        elif action == "Update:":
            new_rarity = command[3]
            plants[plant]["rarity"] = new_rarity
        elif action == "Reset:":
            plants[plant]["rating"].clear()
    else:
        print("error")

print(f"Plants for the exhibition:")
for plant in plants:
    if len(plants[plant]["rating"]) != 0:
        plant_average = sum(plants[plant]["rating"]) / len(plants[plant]["rating"])
    else:
        plant_average = 0
    print(f"- {plant}; Rarity: {plants[plant]['rarity']}; Rating: {plant_average:.2f}")


"""                     Task:
You have now returned from your world tour. On your way, you have discovered some new 
plants, and you want to gather some information about them and create an exhibition to
see which plant is highest rated.

On the first line, you will receive a number n. On the next n lines, you will be given 
some information about the plants that you have discovered in the format: 
"{plant}<->{rarity}". Store that information because you will need it later. 
If you receive a plant more than once, update its rarity.

After that, until you receive the command "Exhibition", 
you will be given some of these commands:
    "Rate: {plant} - {rating}" – add the given rating to the plant (store all ratings)
    "Update: {plant} - {new_rarity}" – update the rarity of the plant with the new one
    "Reset: {plant}" – remove all the ratings of the given plant
Note: If any given plant name is invalid, print "error"

After the command "Exhibition", print the information that you have about the plants in 
the following format:
"Plants for the exhibition:
- {plant_name1}; Rarity: {rarity}; Rating: {average_rating}
- {plant_name2}; Rarity: {rarity}; Rating: {average_rating}
…
- {plant_nameN}; Rarity: {rarity}; Rating: {average_rating}"
The average rating should be formatted to the second decimal place.

Input / Constraints
    You will receive the input as described above
Output
    Print the information about all plants as described above
    
    Input
Arnoldii<->4
Woodii<->7
Welwitschia<->2
Rate: Woodii - 10
Rate: Welwitschia - 7
Rate: Arnoldii - 3
Rate: Woodii - 5
Update: Woodii - 5
Reset: Arnoldii
Exhibition

    Output
Plants for the exhibition:
- Arnoldii; Rarity: 4; Rating: 0.00
- Woodii; Rarity: 5; Rating: 7.50
- Welwitschia; Rarity: 2; Rating: 7.00
"""
