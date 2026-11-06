import random

MAZE_WIDTH = 45
MAZE_HEIGHT = 45
# Maze should always be >15 otherwise the mazes genuinely suck
# so we are in fact gonna have the maze be a MINUMUIM of 51 because i wanna add lots of stuff
# nevermind 51 is too big to fit on my screen
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
                if maze[check_y][check_x] == "O":
                    maze[y + direction[1] // 2][x + direction[0] // 2] = "  "
                    make_maze(maze, check_x, check_y)
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
            else:
                location += "  "
        print(location)