# we are so back fr this time tho
from maze import MAZE_HEIGHT, MAZE_WIDTH
from player import Player
import time

def terminal(character, turns, level):
    print(f"LEVEL {level}")
    print("-" * 50)
    print(f"Turn {turns}")
    print(f"Current HP: {character.health}")
    print(f"Current Potions: {character.potions}")
    print(f"Current Weapon Damage: {character.weaponDMG}")
    print(f"Pickaxe Durability: {character.wall_breaks}")

tim = Player()
#terminal(tim)
# terminal tim
# i keep making myself cry during my speeches at this tournament, i am NOT hittin finals lmao