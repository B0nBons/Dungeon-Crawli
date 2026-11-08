# might have to chance the class since this is kkinda more like a weapon glossary/tracker kinda thing?

class Inventory():
    def __init__(self):
        self.inv = {
            "potions" : 3,
            "pick_durability" : 2,
            "weapons_attained" : { # weapon : obtained, then weapon index will include weapon : damage stats
                "Stick" : {
                    "obtained" : True,
                    "damage" : 2
                },
            "Crumbling Stone Sword" : {
                    "obtained" : False,
                    "damage" : 4
                },
            "Blunt Rapier" : {
                    "obtained" : False,
                    "damage" : 7
                },
            "Trainee's First Sword" : {
                    "obtained" : False,
                    "damage" : 10
                },
            "Polished Dagger" : {
                    "obtained" : False,
                    "damage" : 14
                },
            "Steel Sword" : {
                "obtained" : False,
                "damage" : 17
            },
            "Heavy Claymore" : {
                "obtained" : False,
                "damage" : 20 # may add a speed debuff modifier
            },

            }
        }
    def show(self):
        pass
    # time constraints so i am curently using a kinda bad dict inv for player in the player class
    def add_item(self):
        pass
    def use_item(self):
        pass
    def trash_item(self):
        pass