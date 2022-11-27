cities = {}

while True:
    command = input().split("||")
    if command[0] == "Sail":
        break
    town, people, gold = command
    if town not in cities:
        cities[town] = [0, 0]
    cities[town][0] += int(people)
    cities[town][1] += int(gold)

while True:
    command = input().split("=>")
    if command[0] == "End":
        break
    action = command[0]
    if action == "Plunder":
        town, people, gold = command[1:]
        if cities[town][0] > 0 and cities[town][1] > 0:
            cities[town][0] -= int(people)
            cities[town][1] -= int(gold)
            print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
            if cities[town][0] == 0 or cities[town][1] == 0:
                del cities[town]
                print(f"{town} has been wiped off the map!")
    elif action == "Prosper":
        town, gold = command[1:]
        if int(gold) > 0:
            cities[town][1] += int(gold)
            print(
                f"{gold} gold added to the city treasury. "
                f"{town} now has {cities[town][1]} gold.")
        else:
            print("Gold added cannot be a negative number!")

if cities:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for city in cities:
        print(
            f"{city} -> "
            f"Population: {cities[city][0]} citizens, Gold: {cities[city][1]} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")


"""                     Task:
Anno 1681. The Caribbean. The golden age of piracy. You are a well-known pirate 
captain by the name of Jack Daniels. Together with your comrades Jim (Beam) and 
Johnny (Walker), you have been roaming the seas, looking for gold and treasure… and 
the occasional killing, of course. Go ahead, target some wealthy settlements and show 
them the pirate's way!

Until the "Sail" command is given, you will be receiving:
    You and your crew have targeted cities, with their population and gold, 
        separated by "||".
    If you receive a city that has already been received, you have to increase the 
        population and gold with the given values.
After the "Sail" command, you will start receiving lines of text representing events 
until the "End" command is given. 

Events will be in the following format:

"Plunder=>{town}=>{people}=>{gold}"
    You have successfully attacked and plundered the town, killing the given number of 
        people and stealing the respective amount of gold. 
    For every town you attack print this message: "{town} plundered! {gold} gold stolen,
        {people} citizens killed."
    If any of those two values (population or gold) reaches zero, the town is disbanded.
    You need to remove it from your collection of targeted cities and print the 
        following message: "{town} has been wiped off the map!"
    There will be no case of receiving more people or gold than there is in the city.
"Prosper=>{town}=>{gold}"
    There has been dramatic economic growth in the given city, increasing its treasury 
        by the given amount of gold.
    The gold amount can be a negative number, so be careful. If a negative amount of 
        gold is given, print: "Gold added cannot be a negative number!" and 
        ignore the command.
    If the given gold is a valid amount, increase the town's gold reserves by the 
        respective amount and print the following message: "{gold added} gold added to 
        the city treasury. {town} now has {total gold} gold."
Input
    On the first lines, until the "Sail" command, you will be receiving strings 
        representing the cities with their gold and population, separated by "||"
    On the following lines, until the "End" command, you will be receiving strings 
        representing the actions described above, separated by "=>"
Output
After receiving the "End" command, if there are any existing settlements on your list 
of targets, you need to print all of them, in the following format:
    "Ahoy, Captain! There are {count} wealthy settlements to go to:
    {town1} -> Population: {people} citizens, Gold: {gold} kg
    {town2} -> Population: {people} citizens, Gold: {gold} kg
    …
    {town…n} -> Population: {people} citizens, Gold: {gold} kg"
If there are no settlements left to plunder, print:
    "Ahoy, Captain! All targets have been plundered and destroyed!"
Examples
            Input                       Output
Tortuga||345000||1250               Tortuga plundered! 380 gold stolen,
Santo Domingo||240000||630              75000 citizens killed.
Havana||410000||1100                180 gold added to the city treasury. 
Sail                                    Santo Domingo now has 810 gold.
Plunder=>Tortuga=>75000=>380        Ahoy, Captain! There are 3 wealthy settlements to 
Prosper=>Santo Domingo=>180             go to:
End                                 Tortuga -> Population: 270000 citizens, Gold: 870 kg
                                    Santo Domingo -> Population: 240000 citizens, 
                                        Gold: 810 kg
                                    Havana -> Population: 410000 citizens, Gold: 1100 kg
"""