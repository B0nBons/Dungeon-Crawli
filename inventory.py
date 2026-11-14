# yeah so its not a class now lol
# from SOMETHING import owned weapons
# actually nvm im a chud

weapons = {
    "Stick" : {
        "obtained" : True,
        "damage" : 2,
        "rarity" : "common"},
        
    "Crumbling Stone Sword" : {
        "obtained" : False,
        "damage" : 4,
        "rarity" : "common"}, # i hate reformatting, ts is genuinely waste of time

    "Blunt Rapier" : {
        "obtained" : False,
        "damage" : 7,
        "rarity" : "uncommon"},

    "Trainee's First Sword" : {
        "obtained" : False,
        "damage" : 10,
        "rarity" : "uncommon"},

    "Polished Dagger" : {
        "obtained" : False,
        "damage" : 14,
        "rarity" : "rare"},

    "Steel Sword" : {
        "obtained" : False,
        "damage" : 17,
        "rarity" :"rare"},

    "Heavy Claymore" : {
        "obtained" : False,
        "damage" : 20,
        "rarity" : "epic"}} # REMEMBER THE SPEED VAL BEING RELEVANT

def get_damage(weapon):
    if weapon in weapons:
        return weapons[weapon]["damage"]
    else:
        print("Oddly enough, it appears as if this weapon is not a weapon at all.")
        return IndexError
    # i lowk dont know if you can just return errs like this but who knows

def show_obtained_weapons(owned):
    print("- - - OBTAINED WEAPONS - - -")
    # we ARE gettin slimed out
    for weapon, info in weapons.items(): # i miss items.items
        if weapon in owned:
            print(f"{weapon}: {info['damage']} damage. {info['rarity'].upper()}")
        else:
            pass