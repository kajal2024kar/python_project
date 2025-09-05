import time
import os

# Snake body (list of [x, y])
snake = [[5, 5], [4, 5], [3, 5]]
direction = "RIGHT"

# Game area size
width, height = 20, 10

def print_board(snake):
    os.system("cls" if os.name == "nt" else "clear")  # clear screen
    for y in range(height):
        for x in range(width):
            if [x, y] in snake:
                print("O", end="")  # snake body
            else:
                print(".", end="")  # empty space
        print()
    print("Snake:", snake)

while True:
    # Move head
    head = snake[0].copy()
    if direction == "UP":
        head[1] -= 1
    elif direction == "DOWN":
        head[1] += 1
    elif direction == "LEFT":
        head[0] -= 1
    elif direction == "RIGHT":
        head[0] += 1

    # Insert new head
    snake.insert(0, head)
    # Remove tail (so snake doesn't grow endlessly)
    snake.pop()

    # Print board
    print_board(snake)

    time.sleep(0.3)  # control speed
