# idk

class Inventory():
    def __init__(self):
        self.inv = {
            "potions" : 3,
            "pick_durability" : 2,
            "weapons_attained" : { # weapon : obtained, then weapon index will include weapon : damage stats
                "Stick" : True,
                "Crumbling Stone Sword" : False,
                "Blunt Rapier" : False,
                "Trainee's First Sword" : False,
                "Polished Dagger" : False,

            }
        }
    def show(self):
        pass
    def add_item(self):
        pass
    def use_item(self):
        pass
    def trash_item(self):
        pass