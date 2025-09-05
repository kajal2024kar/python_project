import random

# Initialize board
board = ["-"] * 9

# Function to print the board
def print_board(board):
    print(f"{board[0]} || {board[1]} || {board[2]}")
    print(f"{board[3]} || {board[4]} || {board[5]}")
    print(f"{board[6]} || {board[7]} || {board[8]}")
    print()

# Function to check for winner
def check_winner(board, mark):
    win_pos = [
        [0,1,2], [3,4,5], [6,7,8],  # Rows
        [0,3,6], [1,4,7], [2,5,8],  # Columns
        [0,4,8], [2,4,6]            # Diagonals
    ]
    for pos in win_pos:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == mark:
            return True
    return False

# Function to check for draw
def is_draw(board):
    return "-" not in board

# Game loop
while True:
    print_board(board)

    # Player move
    while True:
        try:
            move = int(input("Enter your position (1-9): "))
            if 1 <= move <= 9 and board[move - 1] == "-":
                board[move - 1] = "X"
                break
            else:
                print("🚫 Invalid or taken position. Try again.")
        except ValueError:
            print("❌ Enter a valid number.")

    # Check for player win
    if check_winner(board, "X"):
        print_board(board)
        print("🎉 You Win!")
        break

    if is_draw(board):
        print_board(board)
        print("🤝 It's a Draw!")
        break

    # Computer move
    while True:
        com = random.randint(0, 8)
        if board[com] == "-":
            board[com] = "O"
            print(f"Computer chose position {com + 1}")
            break

    # Check for computer win
    if check_winner(board, "O"):
        print_board(board)
        print("💻 Computer Wins!")
        break

    if is_draw(board):
        print_board(board)
        print("🤝 It's a Draw!")
        break
