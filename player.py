# we are so back
# idk if i wanna class player or func player, so fn its GOnna be a class to make it 

class Player():
    def __init__(self):
        self.health = 100
        self.max_health = 100
        self.potions = 3
        # healing and health baased stuff

        self.weaponDMG = 5
        self.wall_breaks = 2
        self.items = {
            "Potions" : self.potions,
            "Weapon Damage" : self.weaponDMG,
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

    def inventory(self, add_item=False, remove_item=False):
        # if both keyargs are false, then assume player is gonna check inv
        if add_item == False and remove_item == False:
            for key, val in self.items.items(): # top ten WORST names omg
                print(f"{key} : {val}")