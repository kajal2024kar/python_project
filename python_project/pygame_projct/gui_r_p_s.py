import pygame
import sys
import random

choi = ["Rock", "Paper", "Scissors"]
comp_sc = 0
player_sc = 0

# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()

# Set up display
window = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Rock 🪨 Paper 🗞️ Scissors ✂️")

# Define colors
WHITE = (255, 255, 255)
colour = "#5d9a12"
BLACK = (0, 0, 0)

# Font
font = pygame.font.SysFont(None, 40)

# Buttons
rock_rect = pygame.Rect(50, 250, 200, 80)
paper_rect = pygame.Rect(300, 250, 200, 80)
scissors_rect = pygame.Rect(550, 250, 200, 80)

# Game state
computer_choice = ""
player_choice = ""
result_text = ""

# Draw button function
def draw_button(window, colour, button_rect, text="Click me"):
    pygame.draw.rect(window, colour, button_rect, border_radius=10)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=button_rect.center)
    window.blit(text_surface, text_rect)

# Draw text function
def draw_text(text, font, colour, x, y):
    te = font.render(text, True, colour)
    window.blit(te, (x, y))

# Main loop
while True:
    window.fill(WHITE)

    # Draw buttons
    draw_button(window, colour, rock_rect, "Rock")
    draw_button(window, colour, paper_rect, "Paper")
    draw_button(window, colour, scissors_rect, "Scissors")

    # Show result and score
    if result_text:
        draw_text(f"{result_text}   Computer: {comp_sc}   Player: {player_sc}", font, BLACK, 40, 400)
        draw_text(f"Player: {player_choice} | Computer: {computer_choice}", font, BLACK, 40, 450)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            computer_choice = random.choice(choi)
            result_text = ""
            player_choice = ""

            if rock_rect.collidepoint(event.pos):
                player_choice = "Rock"
                if computer_choice == "Scissors":
                    result_text = "You Win!"
                    player_sc += 1
                elif computer_choice == "Paper":
                    result_text = "You Lose!"
                    comp_sc += 1
                else:
                    result_text = "It's a Draw!"

            elif paper_rect.collidepoint(event.pos):
                player_choice = "Paper"
                if computer_choice == "Rock":
                    result_text = "You Win!"
                    player_sc += 1
                elif computer_choice == "Scissors":
                    result_text = "You Lose!"
                    comp_sc += 1
                else:
                    result_text = "It's a Draw!"

            elif scissors_rect.collidepoint(event.pos):
                player_choice = "Scissors"
                if computer_choice == "Paper":
                    result_text = "You Win!"
                    player_sc += 1
                elif computer_choice == "Rock":
                    result_text = "You Lose!"
                    comp_sc += 1
                else:
                    result_text = "It's a Draw!"

    clock.tick(60)
    pygame.display.update()