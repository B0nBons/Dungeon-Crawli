## An Adventure With Search Algorithms

For the longest time, I heard of search algorithims. I knew that they all had one goal in mind. To search (wow). 
But I never actually bothered looking into how they work, or the intricate differences in each one. Therefore, in order to force myself to learn how search algos work, I decided to make a simple game -- Dungeon Crawli (...the name is TBD still. It's a placeholder.)

<img width="523" height="468" alt="Screenshot 2026-11-08 3 54 42 PM" src="https://github.com/user-attachments/assets/cdd3bbd7-f568-447c-aef4-5c2651bc269d" />

Quick Note!
This will likely only be playable on linux systems, since I do NOT want to setup a windows packager on github actions!!!

## How to Install
First, download the linux release [here](https://github.com/B0nBons/Dungeon-Crawli/releases/tag/1.0.0). Once you've downloaded that, navigate to your terminal (this can be opened by pressing ctrl + alt + t). Run the following in the terminal (depending on where you downloaded it, navigate into that folder by using `cd FOLDER` where FOLDER is where the download is).

```
chmod +x ./main
```
Then, to start the game, run the following
```
./main
```

## How to Play

Run the linux binary. Some linux distros will require you to open the terminal, write "chmod +x ./BINARY" where BINARY is whatever the binary is called when it downloads to your laptop. Then, run ./BINARY to run the game. It is terminal based! (inherently, the binary is just called main)

![how the game looks](<Screenshot 2026-11-08 3.54.42 PM.png>)

As soon as you run the binary, you'll see a little flower stuck in a maze. That flower is YOU! Your goal is to get to the exit of the maze in as few turns as possible. Some things to know:

▩ - This is a wall. Sadly, your game character still hasn't learned how to walk through walls, so they must be avoided.
▢ - Depending on your font, these will either render as two, narrow boxes (which you can see in the image above), or as two normal, square sized boxes. You CAN break these. However, you must decide when breaking them would benefit you, as you are only able to break two of these walls total.

Currently, the game does have an inventory system, as well as math logic for loot from chests. Due to personal stuff, I wasn't able to fully implement that, but they will be implemented in the next version! For now, this acts as an infinite maze generator- is there a chance that you'll see the same maze? Yes, however it is EXTREMELY unlikely. You also have potions that you can drink, if you'd like to waste a turn (potions will be very relevant later). 

## Tech Stack
This was written fully in Python (3.14)! It also currently uses:
- random (for many functions, such as maze generation, shuffling, and more)!
