import pygame
import random

# Initialize board
board = ["-"] * 9
player_turn = True
game_over = False

# Screen size
WIDTH, HEIGHT = 800, 800
GRID_HEIGHT = 720  # Leave space for reset button
BUTTON_HEIGHT = 80

# Colors
LINE_COLOR = (0, 0, 0)
BG_COLOR = (255, 255, 255)
X_COLOR = (255, 0, 0)
O_COLOR = (0, 0, 255)
FONT_SIZE = 120
RESULT_FONT_SIZE = 60

# Pygame setup
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
font = pygame.font.SysFont(None, FONT_SIZE)
result_font = pygame.font.SysFont(None, RESULT_FONT_SIZE)

# Reset button
reset_button = pygame.Rect(250, GRID_HEIGHT + 10, 300, 50)

def draw_button(window, colour, button_rect, text="Click me"):
    pygame.draw.rect(window, colour, button_rect, border_radius=10)
    text_surface = result_font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=button_rect.center)
    window.blit(text_surface, text_rect)

def check_winner(board, mark):
    win_pos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for pos in win_pos:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == mark:
            return True
    return False

def is_draw(board):
    return "-" not in board

def draw_board(window, board):
    window.fill(BG_COLOR)
    # Grid lines
    pygame.draw.line(window, LINE_COLOR, (WIDTH // 3, 0), (WIDTH // 3, GRID_HEIGHT), 5)
    pygame.draw.line(window, LINE_COLOR, (2 * WIDTH // 3, 0), (2 * WIDTH // 3, GRID_HEIGHT), 5)
    pygame.draw.line(window, LINE_COLOR, (0, GRID_HEIGHT // 3), (WIDTH, GRID_HEIGHT // 3), 5)
    pygame.draw.line(window, LINE_COLOR, (0, 2 * GRID_HEIGHT // 3), (WIDTH, 2 * GRID_HEIGHT // 3), 5)

    # Draw X and O
    for i in range(9):
        mark = board[i]
        if mark != "-":
            row = i // 3
            col = i % 3
            x = col * (WIDTH // 3) + WIDTH // 6
            y = row * (GRID_HEIGHT // 3) + GRID_HEIGHT // 6
            color = X_COLOR if mark == "X" else O_COLOR
            text = font.render(mark, True, color)
            text_rect = text.get_rect(center=(x, y))
            window.blit(text, text_rect)

def show_result(text):
    message = result_font.render(text, True, (0, 0, 0))
    rect = message.get_rect(center=(WIDTH // 2, HEIGHT - 80))
    window.blit(message, rect)

# Main loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # Reset button
        if event.type == pygame.MOUSEBUTTONDOWN:
            if reset_button.collidepoint(event.pos):
                board = ["-"] * 9
                player_turn = True
                game_over = False

        if event.type == pygame.MOUSEBUTTONDOWN and player_turn and not game_over:
            x, y = event.pos
            if y < GRID_HEIGHT:
                row = y // (GRID_HEIGHT // 3)
                col = x // (WIDTH // 3)
                index = row * 3 + col
                if board[index] == "-":
                    board[index] = "X"
                    player_turn = False
                    if check_winner(board, "X") or is_draw(board):
                        game_over = True

    # Computer move
    if not player_turn and not game_over:
        empty = [i for i in range(9) if board[i] == "-"]
        if empty:
            pygame.time.delay(300)
            comp_move = random.choice(empty)
            board[comp_move] = "O"
            player_turn = True
            if check_winner(board, "O") or is_draw(board):
                game_over = True

    draw_board(window, board)
    draw_button(window, (128, 128, 128), reset_button, "RESET")

    if game_over:
        if check_winner(board, "X"):
            show_result("🎉 You Win!")
        elif check_winner(board, "O"):
            show_result("😞 Computer Wins!")
        else:
            show_result("🤝 It's a Draw!")

    pygame.display.update()

pygame.quit()
