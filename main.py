import playsound
from maze import make_maze, show_maze, init_maze, breakable_wall, MAZE_WIDTH, MAZE_HEIGHT
from log import terminal
from player import Player

# it is now printing something, but not enough of something

# since the maze printing function works (!!) i'm now going to start working on making random mazes everytime, which I think is where dfs (depth first search) comes in??? or ill use that to make the exit always be the farthest from possible from the entrance
# that is honestly a disgustingly long comment
player_startX = 1
player_startY = 1
exit_X = MAZE_WIDTH - 2
exit_Y = MAZE_HEIGHT - 2


# this is the MAIN game loop (we love while true)
def mainLoop():
    global player_startY, player_startX, exit_X, exit_Y
    maze = breakable_wall(make_maze((init_maze())))
    little_timmy = Player()
    # like an onion    
    while True:
        # something like next level screen

        # idk

        show_maze(player_startX, player_startY, exit_X, exit_Y, maze)
        
        # now i get why we want short variable names, my fingers HURT
        if player_startX == exit_X and player_startY == exit_Y:
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
        attempt_moveX = player_startX
        attempt_moveY = player_startY

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
            print("The wall is still there. No matter how much you attempt to walk through it, it refuses to move.")

        # yes guys it works !!! :D
        elif maze[attempt_moveY][attempt_moveX] == "B": # guys its not acting like a wall help
            print("A wall. Made of rocks, it seems like it would fall with a strong hit...")
            little_timmy.wall_break(attempt_moveX, attempt_moveY, maze)

        else:
            player_startX = attempt_moveX
            player_startY = attempt_moveY

if __name__ == "__main__":
    mainLoop()