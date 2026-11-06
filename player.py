# we are so back
# idk if i wanna class player or func player, so fn its GOnna be a class to make it 

class Player():
    def __init__(self):
        self.health = 100
        self.max_health = 100
        self.potions = 3
        self.weaponDMG = 5

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
        if self.potions > 5:
            print(f"You have more than enough anyway. Healed {heal} HP.")
            self.health += heal
            if self.health > self.max_health:
                self.health = self.max_health
        elif 3 < self.potions <= 5:
            print(f"Down the hatch. Healed {heal} HP.")
            self.health += heal
            if self.health > self.max_health:
                self.health = self.max_health
        elif 1 <= self.potions <= 3:
            print(f"Better alive with no potions than the latter. Healed {heal} HP.")
            self.health += heal
            if self.health > self.max_health:
                self.health = self.max_health