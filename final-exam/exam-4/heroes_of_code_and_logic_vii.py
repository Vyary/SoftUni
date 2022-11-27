MAX_HP = 100
MAX_MP = 200


def hero_recorder(heroes, hero_full_stats):
    hero, hp, mp = hero_full_stats
    heroes[hero] = {"hp": int(hp), "mp": int(mp)}


def cast_spell(heroes, hero, mp_needed, spell):
    if heroes[hero]["mp"] >= int(mp_needed):
        heroes[hero]["mp"] -= int(mp_needed)
        return (
            f"{hero} has successfully cast {spell} and now has {heroes[hero]['mp']} MP!"
        )
    else:
        return f"{hero} does not have enough MP to cast {spell}!"


def take_damage(heroes, hero, damage, attacker):
    if heroes[hero]["hp"] > int(damage):
        heroes[hero]["hp"] -= int(damage)
        return (
            f"{hero} was hit for {damage} HP by {attacker} and now "
            f"has {heroes[hero]['hp']} HP left!"
        )
    else:
        del heroes[hero]
        return f"{hero} has been killed by {attacker}!"


def recharge(heroes, hero, restored_mp):
    hero_mp = heroes[hero]["mp"]
    hero_mp += int(restored_mp)
    if hero_mp > MAX_MP:
        restored = MAX_MP - heroes[hero]["mp"]
        heroes[hero]["mp"] = MAX_MP
        return f"{hero} recharged for {restored} MP!"
    else:
        heroes[hero]["mp"] = hero_mp
        return f"{hero} recharged for {restored_mp} MP!"


def heal(heroes, hero, restored_hp):
    hero_hp = heroes[hero]["hp"]
    hero_hp += int(restored_hp)
    if hero_hp > MAX_HP:
        restored = MAX_HP - heroes[hero]["hp"]
        heroes[hero]["hp"] = MAX_HP
        return f"{hero} healed for {restored} HP!"
    else:
        heroes[hero]["hp"] = hero_hp
        return f"{hero} healed for {restored_hp} HP!"


def main():
    number_of_heroes = int(input())
    heroes = {}
    for _ in range(number_of_heroes):
        hero_full_stats = input().split()
        hero_recorder(heroes, hero_full_stats)

    while True:
        full_action = input().split(" - ")
        if full_action[0] == "End":
            break

        action, hero, amount = full_action[:3]
        if action == "CastSpell":
            spell_name = full_action[3]
            print(cast_spell(heroes, hero, amount, spell_name))
        elif action == "TakeDamage":
            attacker = full_action[3]
            print(take_damage(heroes, hero, amount, attacker))
        elif action == "Recharge":
            print(recharge(heroes, hero, amount))
        elif action == "Heal":
            print(heal(heroes, hero, amount))

    for hero in heroes:
        print(hero)
        print(f"HP: {heroes[hero]['hp']}")
        print(f"MP: {heroes[hero]['mp']}")


if __name__ == "__main__":
    main()


"""                     Task:
You got your hands on the most recent update on the best MMORPG of all time – 
Heroes of Code and Logic. You want to play it all day long! So cancel all other 
arrangements and create your party!

On the first line of the standard input, you will receive an integer n – the number of
heroes that you can choose for your party. On the next n lines, the heroes themselves 
will follow with their hit points and mana points separated by a single space in 
the following format: 

"{hero name} {HP} {MP}"
    HP stands for hit points and MP for mana points
    a hero can have a maximum of 100 HP and 200 MP

After you have successfully picked your heroes, you can start playing the game. 
You will be receiving different commands, each on a new line, separated by " – ", 
until the "End" command is given. 
There are several actions that the heroes can perform:

"CastSpell – {hero name} – {MP needed} – {spell name}"
    If the hero has the required MP, he casts the spell, thus reducing his MP. 
    Print this message:
        "{hero name} has successfully cast {spell name} and 
        now has {mana points left} MP!"
    If the hero is unable to cast the spell print:
        "{hero name} does not have enough MP to cast {spell name}!"
        
"TakeDamage – {hero name} – {damage} – {attacker}"
    Reduce the hero HP by the given damage amount. 
        If the hero is still alive (his HP is greater than 0) print:
    "{hero name} was hit for {damage} HP by {attacker} and 
        now has {current HP} HP left!"
    If the hero has died, remove him from your party and print:
        "{hero name} has been killed by {attacker}!"
        
"Recharge – {hero name} – {amount}"
    The hero increases his MP. If it brings the MP of the hero above the maximum 
        value (200), MP is increased to 200. (the MP can't go over the maximum value).
    Print the following message:
        "{hero name} recharged for {amount recovered} MP!"
        
"Heal – {hero name} – {amount}"
    The hero increases his HP. If a command is given that would bring the HP of the
        hero above the maximum value (100), HP is increased to 100 (the HP can't go 
        over the maximum value).
    Print the following message:
        "{hero name} healed for {amount recovered} HP!"
        
Input
    On the first line of the standard input, you will receive an integer n
    On the following n lines, the heroes themselves will follow with their hit 
        points and mana points separated by a space in the following format
    You will be receiving different commands, each on a new line, separated by " – ", 
        until the "End" command is given

Output
    Print all members of your party who are still alive, in the following format 
        (their HP/MP need to be indented 2 spaces):
            "{hero name}
            HP: {current HP}
            MP: {current MP}"
            
Constraints
    The starting HP/MP of the heroes will be valid, 32-bit integers will never be 
        negative or exceed the respective limits.
    The HP/MP amounts in the commands will never be negative.
    The hero names in the commands will always be valid members of your party. 
        No need to check that explicitly.

Examples
            Input	                                Output
2
Solmyr 85 120
Kyrre 99 50
Heal - Solmyr - 10                          Solmyr healed for 10 HP!
Recharge - Solmyr - 50                      Solmyr recharged for 50 MP!
TakeDamage - Kyrre - 66 - Orc               Kyrre was hit for 66 HP by Orc and now has 
                                                33 HP left!
CastSpell - Kyrre - 15 - ViewEarth          Kyrre has successfully cast ViewEarth and 
                                                now has 35 MP!
End                                         Solmyr
                                            HP: 95
                                            MP: 170
                                            Kyrre
                                            HP: 33
                                            MP: 35
"""
