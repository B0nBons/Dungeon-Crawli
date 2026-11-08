import math
import random
# wish me luck guys, i gotta place at speech and debate today or ima be so sad
# also if this is the same reviewer, i wanted to continue my rpg but gh codespaces said it was too big :(

def select_chest(luck, misfortune, chest_type = "basic"):
    # luck is, for now, a stat that is fixed, but can be later incr via items
    # its squarerooted to ensure that luckmaxxing doesnt give insane drops easily
    basic_chests = {
        "wooden" : 50,
        "stone" : 20,
        "reinforced" : 15,
        "golden" : 10,
        "diamond" : 5}
    
    lucky_chests = {
        "wooden" : 50 / (1 + math.sqrt(luck)),
        "stone" : 30 / (1 + math.sqrt(luck)),
        "reinforced" : 15 * (1 + math.sqrt(luck)),
        "golden" : 10 * (1 + math.sqrt(luck)),
        "diamond" : 5 * (1 + math.sqrt(luck))}
    
    cursed_chests = {
        "wooden" : 50 * (1 + math.sqrt(misfortune)),
        "stone" : 30 * (1 + math.sqrt(misfortune)),
        "reinforced" : 15 / (1 + math.sqrt(misfortune)),
        "golden" : 10 / (1 + math.sqrt(misfortune)),
        "diamond" : 5 / (1 + math.sqrt(misfortune))}

    if chest_type == "basic" :
        roll = random.randint(0,100)
        if roll <= 50:
            print("this will be a func that actually returns an assortment of items based on chest type")
        elif roll <= 70:
            print("see above")
        elif roll <= 85:
            print("")
        elif roll <= 90:
            print("")
        elif roll <= 100:
            print("")
        else:
            print("This is impossible, you should've never seen this")

    elif chest_type == "lucky":
        # this is so annoying but i can only code in these stupid little bursts bc i keep getting called for rounds, and thats gonna make the cute nice hackatime gradient map thing look so ugly, ts pmo
        pass
    # for now, i dont think lucky/misfortune chests will be implemented until I can make an armor system kinda thing