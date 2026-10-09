"""Simple 2D grid game prototype - move a player with w/a/s/d to reach a goal."""
import sys

def main():
    width, height = 5, 5
    grid = [['.' for _ in range(width)] for _ in range(height)]
    player = [0, 0]
    goal = [height-1, width-1]
    grid[player[0]][player[1]] = '@'
    grid[goal[0]][goal[1]] = 'G'
    while True:
        for row in grid:
            print(' '.join(row))
        if player == goal:
            print("You reached the goal!")
            break
        move = input("Move (w/a/s/d): ").lower()
        if move not in 'wasd':
            print("Invalid move. Use w/a/s/d.")
            continue
        dy, dx = 0, 0
        if move == 'w': dy = -1
        if move == 's': dy = 1
        if move == 'a': dx = -1
        if move == 'd': dx = 1
        new_y, new_x = player[0]+dy, player[1]+dx
        if 0 <= new_y < height and 0 <= new_x < width:
            grid[player[0]][player[1]] = '.'
            player = [new_y, new_x]
            grid[player[0]][player[1]] = '@'
        else:
            print("Can't move outside the grid.")

if __name__ == "__main__":
    main()