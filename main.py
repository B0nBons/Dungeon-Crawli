import playsound
import random

MAZE_WIDTH = 15
MAZE_HEIGHT = 15
# Maze should always be >15 otherwise the mazes genuinely suck

player_startX = 1
player_startY = 1
exit_X = MAZE_WIDTH - 2
exit_Y = MAZE_HEIGHT - 2

maze = []

for ROW in range(MAZE_HEIGHT):
    row = []
    for THINGINROW in range(MAZE_WIDTH):
        row.append("O")
    maze.append(row)

# Setup base maze of _ width and _ height (can change later/make into a func)

# will do custom start/endpoint later (so that endpoint is alwas=ys very far from start)
def MAKE_MAZE(x=1,y=1):
    # xy is just starting location
    maze[y][x] = " "
    goto = [
        [0, -2],
        [-2, 0],
        [2, 0],
        [0, 2]]
    random.shuffle(goto)

    for direction in goto:
        check_x = x + direction[0]
        check_y = y + direction[1]

        if 0 < check_x < (MAZE_WIDTH - 1):
            if 0 < check_y < (MAZE_HEIGHT - 1):
                if maze[check_y][check_x] == "O":
                    maze[y + direction[1] // 2][x + direction[0] // 2] = "  "
                    MAKE_MAZE(check_x, check_y)

def SHOWmaze(player_x, player_y, exit_x, exit_y):
    for y in range(MAZE_HEIGHT):
        location = ""
        for x in range(MAZE_WIDTH):
            if x == player_x and y == player_y:
                location += "✿ "
                # theres allegedly no unicode person so placehold is a flower lol
            elif x == exit_x and y == exit_y:
                location += "E " # e for exit bc only 1 char should be added
            elif maze[y][x] == "O":
                location += "▩ " # idk man looked cute
            else:
                location += "  "
        print(location)

MAKE_MAZE(1,1)
SHOWmaze(player_startX, player_startY, exit_X, exit_Y)



# it is now printing something, but not enough of something

# since the maze printing function works (!!) i'm now going to start working on making random mazes everytime, which I think is where dfs (depth first search) comes in??? or ill use that to make the exit always be the farthest from possible from the entrance
# that is honestly a disgustingly long comment


# this is the MAIN game loop (we love while true)
def mainLoop():

    while True:
        SHOWmaze()
        if player_x == exit_x and player_y == exit_y:
            print("yippee")

        # i think ill add potions and stuff to this, but for now its only gonna be movement
        # this sub is so mean for no reason lmaoo
        # so irrelevant to code but i think this will actually make a reviewer laugh
        # so this sub for ib glopol is taking phones (teachers can leave special instructions that kids can listen to music on their phones, whatever etc,)
        # as soon as she steps out with a bunch of peoples phones, the entire class starts to talk
        # turns out she was testing us or som and just start going "ch ch ch" really mad and said seriously
        # but ffs its a class centered around discussion and collaboration, like girl our teach never said to just force us to shut up and be quiet lmao
        # yeah anyway hope that was funny

        movement = input("WASD (Up/Down/Left/Right)").lower()
        attempt_moveX = player_x
        attempt_moveY = player_y

        if movement == "w":
            attempt_moveY -= 1
        elif movement == "s":
            attempt_moveY += 1
        elif movement == "a":
            attempt_moveX -= 1
        elif movement == "d":
            attempt_moveX += 1 
        else:
            print("Invalid option (w/a/s/d)")

        if maze[attempt_moveY][attempt_moveX] == "O":
            print("That is in fact a wall")
        else:
            player_x = attempt_moveX
            player_y = attempt_moveY