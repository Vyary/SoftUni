# The force users struggle to remember which side is the different force users from because they switch them too often.
# So you are tasked to create a web application to manage their profiles. You should store information for every
# unique force user registered in the application.
# You will receive several input lines in one of the following formats:
# "{force_side} | {force_user}"
# "{force_user} -> {force_side}"
# The "force_user" and "force_side" are strings, containing any character.
# If you receive "force_side | force_user":
# •	If there is no such force user and no such force side -> create a new force side and add the force user to
# the corresponding side.
# •	Only if there is no such force user in any force side -> add the force user to the corresponding side.
# •	If there is such force user already -> skip the command and continue to the next operation.
# If you receive a "force_user -> force_side":
# •	If there is such force user already -> change their side.
# •	If there is no such force user in any force side -> add the force user to the corresponding force side.
# •	If there is no such force user and no such force side -> create new force side and add
# the force user to the corresponding side.
# •	Then you should print on the console: "{force_user} joins the {force_side} side!".
# You should end your program when you receive the command "Lumpawaroo". At that point,
# you should print each force side. For each side, print the force users.
# In case there are no force users on a side, you shouldn't print the side information.
# Input / Constraints
# •	The input comes in the form of commands in one of the formats specified above.
# •	The input ends when you receive the command "Lumpawaroo".
# Output
# •	As output for each force side, you must print all the force users.
# •	The output format is:
# "Side: {force_side}, Members: {force_users_count}
# ! {force_user1}
# ! {force_user2}
# …
# ! {force_userN}"
# •	In case there are NO force users on a side, don't print this side.

forces = {}


def add_side_to_forces(force_side):
    if force_side not in forces:
        forces[force_side] = []


def add_user_to_side(user, force_side):
    forces[force_side].append(user)


def does_user_has_side(user, remove_user='No'):
    for force_side, force_users in forces.items():
        if user in force_users:
            if remove_user == 'Yes':
                forces[force_side].remove(user)
            return True
    return False


while True:
    entry = input()
    if entry == 'Lumpawaroo':
        break
    if ' | ' in entry:
        side, name = entry.split(' | ')
        add_side_to_forces(side)
        if does_user_has_side(name) is False:
            forces[side].append(name)
    elif ' -> ' in entry:
        name, side = entry.split(' -> ')
        add_side_to_forces(side)
        if does_user_has_side(name) is False:
            forces[side].append(name)
            print(f"{name} joins the {side} side!")
        elif does_user_has_side(name, 'Yes') is True:
            forces[side].append(name)
            print(f"{name} joins the {side} side!")

for side, users in forces.items():
    if len(forces[side]) > 0:
        print(f"Side: {side}, Members: {len(forces[side])}")
        for name in users:
            print(f'! {name}')
