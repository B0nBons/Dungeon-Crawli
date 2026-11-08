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

def new_dungeon():
    return breakable_wall(make_maze(init_maze))
# to make it actually playable and a loop, we need to have a func that can just spam mazes

# this is the MAIN game loop (we love while true)
def mainLoop():
    global player_startY, player_startX, exit_X, exit_Y
    little_timmy = Player()
    level = 1
    turns = 0

    while little_timmy.alive == True:
        # something like next level screen
        maze = new_dungeon()
        level_completed = False
        player_startX = 1
        player_startY = 1

        while True:
            show_maze(player_startX, player_startY, exit_X, exit_Y, maze)
            terminal(little_timmy, turns, level)
            
            # now i get why we want short variable names, my fingers HURT
            if player_startX == exit_X and player_startY == exit_Y:
                print(f"Level {level} of many has been completed")

            movement = input("WASD (Up/Down/Left/Right) / P (Potion) / I (Inventory)").lower()
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
            # might make this into a func just to keep the main loop organised, but well see

            elif movement == "p":
                little_timmy.use_potion()
                turns += 1

            elif movement == "i": # i should rename movement bc its not even movemnt now, its just all the funcs lmao
                little_timmy.inventory()
                garb = input("Press enter to continue...")

            if maze[attempt_moveY][attempt_moveX] == "O":
                print("The wall is still there. No matter how much you attempt to walk through it, it refuses to move.")

            # yes guys it works !!! :D
            elif maze[attempt_moveY][attempt_moveX] == "B": # guys its not acting like a wall help
                print("A wall. Made of rocks, it seems like it would fall with a strong hit...")
                little_timmy.wall_break(attempt_moveX, attempt_moveY, maze)
                turns += 1

            else:
                player_startX = attempt_moveX
                player_startY = attempt_moveY

            if little_timmy.alive != True:
                break

        print("GAME OVER") # lol
        print(f"You reached level {level}")
        print(f"Total turns: {turns}")

        # maybe show stats or feats


if __name__ == "__main__":
    mainLoop()