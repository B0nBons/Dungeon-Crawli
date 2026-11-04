import playsound
import random

MAZE_WIDTH = 7
MAZE_HEIGHT = 7
# dim for square, might make different mazes using /\ and such

maze = [
    ["O", "O", "O", "O", "O", "O", "O"],
    ["O", " ", "O", " ", "O", " ", " "],
    ["O", " ", "O", " ", " ", " ", "O"],
    ["O", " ", " ", " ", " ", "O", "O"],
    ["O", " ", "O", "O", " ", " ", "O"],
    ["O", " ", " ", "O", " ", " ", "O"],
    ["O", "O", "O", "O", "O", "O", "O"]
]
# hardcoding a maze for testing
# yes its ugly but who cares lol

player_x = 1
player_y = 1

exit_x = 6
exit_y = 1 # idk ive not done list stuff in a hot min

def SHOWmaze():
    for y in range(MAZE_HEIGHT):
        location = ""
        for x in range(MAZE_WIDTH):
            if x == player_x and y == player_y:
                location += "✿ "
                # theres allegedly no unicode person so placehold is a flower lol
            elif x == exit_x and y == exit_y:
                location += "E" # e for exit bc only 1 char should be added
            elif maze[y][x] == "O":
                location += "▩ " # idk man looked cute
            else:
                location += "  "
        print(location)

SHOWmaze()
# it is now printing something, but not enough of something