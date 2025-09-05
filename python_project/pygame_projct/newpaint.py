import pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 800
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Freehand Drawing with Mouse")
font = pygame.font.SysFont(None, 20)

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Initial background color
back_graound_colour = WHITE
DRAW_COLOR = BLACK
#draw button
def draw_button(window, colour, button_rect, text="Click me"):
    pygame.draw.rect(window, colour, button_rect, border_radius=10)
    text_surface = font.render(text, True, WHITE if colour != WHITE else BLACK)
    text_rect = text_surface.get_rect(center=button_rect.center)
    window.blit(text_surface, text_rect)

def handle_bg_color(keys, current_bg):
    if keys[pygame.K_w]:
        return WHITE
    if keys[pygame.K_r]:
        return RED
    if keys[pygame.K_g]:
        return GREEN
    if keys[pygame.K_b]:
        return BLUE
    return current_bg

# Colour buttons
black_button = pygame.Rect(60, 0, 50, 50)
red_button = pygame.Rect(0, 0, 50, 50)

# Fill background
win.fill(back_graound_colour)

# Variables
drawing = False
last_pos = None
brush_size = 5
erasing = False

# Main loop
run = True
while run:
    keys = pygame.key.get_pressed()
    new_bg = handle_bg_color(keys, back_graound_colour)
    if new_bg != back_graound_colour:
        back_graound_colour = new_bg
        win.fill(back_graound_colour)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # Start drawing on mouse down
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button
            if red_button.collidepoint(event.pos):
                DRAW_COLOR = RED
                brush_size = 5
                erasing = False
            elif black_button.collidepoint(event.pos):
                DRAW_COLOR = BLACK
                brush_size = 5
                erasing = False
            else:
                drawing = True
                erasing = False
                last_pos = event.pos

        # Eraser button (right mouse button)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            drawing = True
            erasing = True
            brush_size = 50
            last_pos = event.pos

        # Stop drawing on mouse up
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            last_pos = None

        # Mouse motion with button held down
        if event.type == pygame.MOUSEMOTION and drawing:
            color = back_graound_colour if erasing else DRAW_COLOR
            pygame.draw.line(win, color, last_pos, event.pos, brush_size)
            last_pos = event.pos

    draw_button(win, RED, red_button, "RED")
    draw_button(win, BLACK, black_button, "BLACK")
    pygame.display.update()

pygame.quit()