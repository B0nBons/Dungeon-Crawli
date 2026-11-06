# we are so back fr this time tho
from maze import MAZE_HEIGHT, MAZE_WIDTH
from player import Player
import time

def terminal(character, turns):
    print("-" * MAZE_WIDTH)
    # so this is actually way too small so thatll be figured out later
    print(f"Current HP: {character.health}")
    print(f"Current Potions: {character.potions}")
    print(f"Current Weapon Damage: {character.weaponDMG}")


tim = Player()
#terminal(tim)
# terminal tim