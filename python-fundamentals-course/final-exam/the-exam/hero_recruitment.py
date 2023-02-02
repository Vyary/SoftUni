heroes = {}

while True:
    command = input().split()
    if command[0] == "End":
        break
    elif command[0] == "Enroll":
        hero = command[1]
        if hero not in heroes:
            heroes[hero] = []
        else:
            print(f"{hero} is already enrolled.")
    elif command[0] == "Learn":
        hero = command[1]
        spell = command[2]
        if hero in heroes:
            if spell not in heroes[hero]:
                heroes[hero].append(spell)
            else:
                print(f"{hero} has already learnt {spell}.")
        else:
            print(f"{hero} doesn't exist.")
    elif command[0] == "Unlearn":
        hero = command[1]
        spell = command[2]
        if hero in heroes:
            if spell in heroes[hero]:
                heroes[hero].remove(spell)
            else:
                print(f"{hero} doesn't know {spell}.")
        else:
            print(f"{hero} doesn't exist.")
print("Heroes:")
for hero in heroes:
    print(f"== {hero}: ", end="")
    print(", ".join(heroes[hero]))
