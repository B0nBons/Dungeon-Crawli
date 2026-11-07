import random

MAZE_WIDTH = 25
MAZE_HEIGHT = 25
# ok so testing maze size is gonna be 25 since otherwise it wont fit on my screen
# Maze should always be >15 otherwise the mazes genuinely suck
# so we are in fact gonna have the maze be a MINUMUIM of 51 because i wanna add lots of stuff
# weird feeling that large mazes might not always have a reachable exit (it took me FIVE mins to figure out one)

def init_maze():
    maze = []
    for ROW in range(MAZE_HEIGHT):
        row = []
        for THINGINROW in range(MAZE_WIDTH):
            row.append("O")
        maze.append(row)
    return maze
# Setup base maze of _ width and _ height (can change later/make into a func)

# will do custom start/endpoint later (so that endpoint is alwas=ys very far from start)
def make_maze(maze, x=1,y=1):
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
                if maze[check_y][check_x] == "O" or maze[check_y][check_x] == "B": # Otherwise the breakable walls are just surrounded by normal walls (pointless)
                    maze[y + direction[1] // 2][x + direction[0] // 2] = "  "
                    make_maze(maze, check_x, check_y)
    
    return maze

def breakable_wall(maze):
    total_walls = 3
    walls = 0
    allowed_spots = []
    not_allowed = []

    for y in range(MAZE_HEIGHT):
        for x in range(MAZE_WIDTH):
            if x == 0 or x == MAZE_WIDTH - 1 or y == 0 or y == MAZE_HEIGHT - 1:
                not_allowed.append([x,y])
    # ts so inefficient but idk how to make it faster so deal with it (just play with more than 1 byte of ram)
    for y in range(MAZE_HEIGHT):
        for x in range(MAZE_WIDTH):
            if maze[y][x] == "O" and [x, y] not in not_allowed: # not in not knot (idk)
                allowed_spots.append([x,y])

    random.shuffle(allowed_spots)

    for x, y in allowed_spots:
        if walls != total_walls:
            maze[y][x] = "B" # for broken (top ten sad)
            walls += 1
        else:
            break
    return maze

def show_maze(player_x, player_y, exit_x, exit_y, maze):
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
            elif maze[y][x] == "B":
                location += "▢▢"
                # so i tried for a bit and for SOME reason, the font in my vscode refuses to render it as a two block thing ???
            else:
                location += "  "
        print(location)