# HAHAHA GOODBYE PLAYSOUND I HATE YOU import playsound
# wish me luck, i gotta code on my phone 
# this might be the worst thign ive ever done
from maze import make_maze, show_maze, init_maze, breakable_wall, change_maze_dims, MAZE_WIDTH, MAZE_HEIGHT
from log import terminal
from player import Player

# it is now printing something, but not enough of something

# since the maze printing function works (!!) i'm now going to start working on making random mazes everytime, which I think is where dfs (depth first search) comes in??? or ill use that to make the exit always be the farthest from possible from the entrance
# that is honestly a disgustingly long comment
player_startX = 1
player_startY = 1
exit_X = MAZE_WIDTH - 2
exit_Y = MAZE_HEIGHT - 2
# so i think the way for the player start and exit is gonna be bfs search, since that allegedly finds longest path, and we always want the lingest path
# also becaus it would be fun to have dynamic start and end points
# or this could actually be like commecting levels, and "level ups" are just going to a floor above??
# idk wrte gonna put a pin innit

def new_dungeon():
    return breakable_wall(make_maze(init_maze()))
# to make it actually playable and a loop, we need to have a func that can just spam mazes

# this is the MAIN game loop (we love while true)
def mainLoop():
    global player_startY, player_startX, exit_X, exit_Y
    little_timmy = Player()
    level = 1
    turns = 0

    while little_timmy.alive == True:
        # something like next level screen
        # change_maze_dims(2,2)
        maze = new_dungeon()
        level_completed = False
        player_startX = 1
        player_startY = 1

        if level_completed == True:
            level_completed = False

        while True:
            show_maze(player_startX, player_startY, exit_X, exit_Y, maze)
            terminal(little_timmy, turns, level)
            
            # now i get why we want short variable names, my fingers HURT
            if player_startX == exit_X and player_startY == exit_Y:
                print(f"Level {level} of many has been completed")
                level_completed = True
                level += 1
                break
            DONOTMOVE = None
            WALL_BROKEN = None
            movement = input("WASD (Up/Down/Left/Right) / P (Potion) / I (Inventory) ").lower()
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

            if movement == "p":
                little_timmy.use_potion()
                # no clue why but potions incr turn count by 2???? i cant figure out where the other turn count incr is

            if movement == "i": # i should rename movement bc its not even movemnt now, its just all the funcs lmao
                little_timmy.inventory()
                garb = input("Press enter to continue...")
                # ok so i have NO clue why, but for some reason the turn count increases after you check inv??????

            if maze[attempt_moveY][attempt_moveX] == "O": # i think this being an if statement was making the turn count increase erreneously???? no idea but it works as intended now
                print("The wall is still there. No matter how much you attempt to walk through it, it refuses to move.")
                DONOTMOVE = True
                # i dont like how this line shows on the top when it goes to the next turn but idk a fix so ig ill deal w later

            # yes guys it works !!! :D
            if maze[attempt_moveY][attempt_moveX] == "B":
                print("A wall. Made of rocks, it seems like it would fall with a strong hit...")
                if little_timmy.wall_break(attempt_moveX, attempt_moveY, maze) == False:
                    WALL_BROKEN = False
                # seems i overadded turns in many spots

            if DONOTMOVE != True and WALL_BROKEN == None:
                player_startX = attempt_moveX
                player_startY = attempt_moveY
                turns += 1
            elif WALL_BROKEN == False:
                pass

            if little_timmy.alive != True:
                break

        if little_timmy.alive == False:
            print("GAME OVER") # lol
            print(f"You reached level {level}")
            print(f"Total turns: {turns}")

        # maybe show stats or feats


if __name__ == "__main__":
    mainLoop()