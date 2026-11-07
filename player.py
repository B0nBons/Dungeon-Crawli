# we are so back
# idk if i wanna class player or func player, so fn its GOnna be a class to make it 

class Player():
    def __init__(self):
        self.health = 100
        self.max_health = 100
        self.potions = 3
        self.weaponDMG = 5
        self.wall_breaks = 2

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
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
        self.potions -= 1

    def wall_break(self, targetx, targety, maze):
        if self.wall_breaks == 1:
            if maze[targety][targetx] == "B":
                confirm = input("The pickaxe cannot take much more. Break anyway? (y/n)")
                if confirm.lower() == "y" or confirm.lower() == "yes":
                    maze[targety][targetx] = "  "
                    self.wallbreaks -= 1
                    print("The wall crumbles to ashes, taking your pickaxe with it.")
                elif confirm.lower() == "n" or confirm.lower() == "no":
                    print("You save your pickaxe for another day.")
            else:
                print("Seems reinforced. Best to not hit that.")

        elif self.wall_breaks > 1:
            if maze[targety][targetx] == "B":
                confirm = input("The pickaxe would be more than enough to break this wall... Break wall? (y/n)")
                if confirm.lower() == "y" or confirm.lower() == "yes":
                    maze[targety][targetx] = "  "
                    self.wallbreaks -= 1
                    print("The wall quickly crumbles to dust.")
                elif confirm.lower() == "n" or confirm.lower() == "no":
                    print("You spare your pickaxe from destruction.")
                else:
                    print("You decide to play by your own rules. However, you still must conform to choosing (y/n)")
        else:
            print("Your pickaxe is in need of repair. Using it now would be idiotic.")
        # should only trigger when wall breaks is none
        
        # i think this is gonna need me to add in code in the dfs algo to add 1/10 chance or som of a breakable wall
        # pass until thats figured out

        # i actual hate this repetitive ahs block so im gonna redo it
        # im trying to code rn and for some reason my entire hand/arm keeps on just pulsing or som when i type?? idk, but it HURTS