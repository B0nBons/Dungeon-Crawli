import random

ENEMIES = {
    "Goblin" : 
    {"health" : 10,
     "damage" : 4,
     "icon" : "E"} # add in cute icon later
}

def enemy_gen(maze):
    enemies = []
    total_enemies = 0
    while total_enemies != 3:
        x = random.randint(1, len(maze[0]) - 1)
        y = random.randint(1, len(maze) - 2)
        if maze[y][x] == " ":
            enemies.append([x,y])
            total_enemies += 1
    return enemies

def move_enemies(enemies, maze):
    for foe in enemies:
        x = foe[0]
        y = foe[1]
        moveto = [
            [0, 1],
            [0,-1],
            [1,0],
            [-1, 0] # I FOUND YOU STUPID BUG
        ]
        move = random.choice(moveto)
        if maze[y + move[1]][x + move[0]] == " " or maze[y + move[1]][x + move[0]] == "  ":
            foe[0] += move[0]
            foe[1] += move[1]
        elif maze[y + move[1]][x + move[0]] != " " or maze[y+move[1]][x + move[0]] != "  ":
            moved = False
            attempts = 5
            done = 0
            while moved == False:
                move = random.choice(moveto)
                for i in range(attempts):
                    if maze[y + move[1]][x + move[0]] == " " or maze[y + move[1]][x + move[0]] == "  ":
                        foe[0] += move[0]
                        foe[1] += move[1]
                        moved = True
                        break
                done += 1

                if done == attempts:
                    break