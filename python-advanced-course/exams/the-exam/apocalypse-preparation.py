from collections import deque

ITEMS = {"Patch": 30, "Bandage": 40, "MedKit": 100}

textiles = deque(map(int, input().split()))
medicaments = list(map(int, input().split()))

created_items = {}

while textiles and medicaments:
    item_created = False
    current_textile = textiles.popleft()
    current_medicament = medicaments.pop()
    total = current_textile + current_medicament

    for item, requirement in ITEMS.items():

        if total == requirement:

            if item not in created_items:
                created_items[item] = 0
            created_items[item] += 1
            item_created = True
            break

    if not item_created:

        if total > ITEMS["MedKit"]:

            if "MedKit" not in created_items:
                created_items["MedKit"] = 0
            created_items["MedKit"] += 1
            remaining = total - ITEMS["MedKit"]

            if remaining > 0:
                last_medicament = medicaments.pop()
                last_medicament += remaining
                medicaments.append(last_medicament)
        else:
            current_medicament += 10
            medicaments.append(current_medicament)

if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")
elif not textiles:
    print("Textiles are empty.")
else:
    print("Medicaments are empty.")

if created_items:
    for item, amount in sorted(created_items.items(), key=lambda x: (-x[1], x[0])):
        print(f"{item} - {amount}")
if medicaments:
    print("Medicaments left: " + ", ".join(map(str, medicaments[::-1])))
if textiles:
    print("Textiles left: " + ", ".join(map(str, textiles)))
