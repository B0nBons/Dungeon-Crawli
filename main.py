import playsound
<<<<<<< HEAD
from maze import make_maze, show_maze, MAZE_WIDTH, MAZE_HEIGHT
=======
import random
from maze_funcs import maze, make_maze, show_maze, MAZE_HEIGHT, MAZE_WIDTH

# general start positions until they can be randomized

>>>>>>> af6890861052f80afd1b6077ad69cd589873ca2c

# it is now printing something, but not enough of something

# since the maze printing function works (!!) i'm now going to start working on making random mazes everytime, which I think is where dfs (depth first search) comes in??? or ill use that to make the exit always be the farthest from possible from the entrance
# that is honestly a disgustingly long comment
player_startX = 1
player_startY = 1
exit_X = MAZE_WIDTH - 2
exit_Y = MAZE_HEIGHT - 2

maze = make_maze()

# this is the MAIN game loop (we love while true)
def mainLoop():
<<<<<<< HEAD
    global player_startY, player_startX, exit_X, exit_Y
    while True:
        show_maze(player_startX, player_startY, exit_X, exit_Y)
        if player_startX == exit_X and player_startY == exit_Y:
=======

    player_X = 1
    player_Y = 1
    exit_X = MAZE_WIDTH - 2
    exit_Y = MAZE_HEIGHT - 2

    while True:
        show_maze(player_X, player_Y, exit_X, exit_Y)
        if player_X == exit_X and player_Y == exit_Y:
>>>>>>> af6890861052f80afd1b6077ad69cd589873ca2c
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
<<<<<<< HEAD
        attempt_moveX = player_startX
        attempt_moveY = player_startY
=======
        attempt_moveX = player_X
        attempt_moveY = player_Y
>>>>>>> af6890861052f80afd1b6077ad69cd589873ca2c

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
<<<<<<< HEAD
            player_startX = attempt_moveX
            player_startY = attempt_moveY
=======
            player_x = attempt_moveX
            player_y = attempt_moveY
>>>>>>> af6890861052f80afd1b6077ad69cd589873ca2c

if __name__ == "__main__":
    mainLoop()