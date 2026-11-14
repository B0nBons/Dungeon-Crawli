# we are so back
# idk if i wanna class player or func player, so fn its GOnna be a class to make it 
from inventory import weapons, get_damage, show_obtained_weapons

class Player():
    def __init__(self):
        self.health = 100
        self.max_health = 100
        self.potions = 3
        # healing and health baased stuff

        self.owned_weapons = ["Stick"] # undertale ahs
        self.equiped_weapon = "Stick"
        self.weapon_DMG = get_damage(self.equiped_weapon)
        self.wall_breaks = 2

        self.items = {
            "Potions" : self.potions,
            "Weapon" : self.equiped_weapon, # change this to the chestloot weapon name, and then make a func that can translate name to dmg
            "Weapon Damage" : self.weapon_DMG,
            "Pickaxe Durability" : self.wall_breaks # make keys cap so they print nice and i dont have to deal with it
        }
        # general stuff that idk how to categorize
        # so terra isnt loading for me so this is gonna be an insane commit devlog thing lmao

        self.luck_chest = 5
        self.luck_attack = 20
        # rng gambling factors

        self.alive = True

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            self.alive = False # so it can end the game loop
            print("Fatal hit. Game OVER")
        else:
            print(f"Took {damage} damage")

    def use_potion(self):
        # i genuinely cannot freaking spell ffs
        heal = 15 
        # might change later since we all know I suck arse at balancing
        if (self.health + heal) >= self.max_health:
            heal = self.max_health - self.health 
        if self.potions > 5:
            print(f"You have more than enough anyway. Healed {heal} HP.")
            self.health += heal
        elif 3 < self.potions <= 5:
            print(f"Down the hatch. Healed {heal} HP.")
            self.health += heal
        elif 1 <= self.potions <= 3:
            print(f"Better alive with no potions than the latter. Healed {heal} HP.")
            self.health += heal
        elif self.potions <= 0:
            print(f"You have no potions.")
        self.potions -= 1

# i literally just realised how freaking much code i put for all of this
# i REALLY tried to cover EVERY single case wtf

    def wall_break(self, targetx, targety, maze):
        if self.wall_breaks == 1:
            if maze[targety][targetx] == "B":
                confirm = input("The pickaxe cannot take much more. Break anyway? (y/n)")
                if confirm.lower() == "y" or confirm.lower() == "yes":
                    maze[targety][targetx] = "  "
                    self.wall_breaks -= 1
                    print("The wall crumbles to ashes, taking your pickaxe with it.")
                elif confirm.lower() == "n" or confirm.lower() == "no":
                    print("You save your pickaxe for another day.")
                    return False
                else:
                    print("You mumble gibberish. You must conform to choosing (y/n)")
                    return False
            else:
                print("Seems reinforced. Best to not hit that.")
                return False
                # This seemingly will not trigger

        elif self.wall_breaks > 1:
            if maze[targety][targetx] == "B":
                confirm = input("The pickaxe would be more than enough to break this wall... Break wall? (y/n)")
                if confirm.lower() == "y" or confirm.lower() == "yes":
                    maze[targety][targetx] = "  "
                    self.wall_breaks -= 1
                    print("The wall quickly crumbles to dust.")
                elif confirm.lower() == "n" or confirm.lower() == "no":
                    print("You spare your pickaxe from destruction.")
                    return False
                else:
                    print("You decide to play by your own rules. However, you still must conform to choosing (y/n)")
                    return False
        else:
            print("Your pickaxe is in need of repair. Using it now would be idiotic.")
            return False
        # I know the amount of return False statements is almost excessive, but theres genuinely no other way than that to make sure the player doesnt become a ghost and just walk through walls

        # might make add/remove into a seperate func since this is kinda a nuisance to use
        # okay so i figured out why it doesnt work, so im actually just gonna make seperate add/remove functions

    def add_to_inv(self, item, amount_add):
        if item in self.items:
            self.items[item] += amount_add
            print(f"You pick up {amount_add} {item}")
        elif item not in self.items:
            self.items[item] = amount_add
            print(f"You pick up {amount_add} {item}")

    def remove_from_inv(self, item, amount_del):
        if item in self.items:
            if (self.items[item] - amount_del) > 0:
                self.items[item] -= amount_del
                print(f"You drop {amount_del} {item}, you have {self.items[item]} left")
            elif (self.items[item] - amount_del) == 0:
                self.items[item] = 0
                print(f"You drop your last {item}, you now have 0")
            elif (self.items[item] - amount_del) < 0:
                print(f"You do not have enough {item} to drop {amount_del}")
        else:
            print(f"You seemingly do not possess {item}")
# ok guys i swear ill test my code from now on, ts horrid

    def show_inv(self):
        print("✧──────────✧──────────✧")
        for key, val in self.items.items():
            print(f"{key} : {val}")
        print("✧──────────✧──────────✧")
# kinda wish these could be lil containers, but thats ok for now
# rip inventory, 2026-2026

    def get_weapon(self, weapon):
        if weapon in self.owned_weapons:
            print("You have no reason to add more weight to your bag.")
            # ok so i think weapons are just gonna be infinite durability since im lazy
            return False
        elif weapon not in weapons:
            print("...This doesn't even exist.")
            return False
        else:
            print(f"You picked up a {weapon}!")
            print(f"Damage: {weapons[weapon]['damage']}. {weapons[weapon]['rarity']}")
            self.owned_weapons.append(weapon)
            weapons[weapon]['obtained'] = True
            return True

    def show_equipped_tool(self):
        print("- - - - - -")
        print(f"Weapon: {self.equipped_weapon}")
        print(F"Damage: {self.weapon_DMG}")
        print("- - - - - -")

   #  print(f"Tool: {self.}") dont have seperate tools in so has to be added later

# ok now all of this below is gonna be test stuff to make sure im not gonna have a crisis later on testing

p = Player()
p.show_inv()
p.add_to_inv("Crunchy Taco", 1)
p.show_inv()
p.remove_from_inv("Crunchy Taco", 1)

# CHANGE INVENTORY TO SHOW SPECIFIC WEAPON