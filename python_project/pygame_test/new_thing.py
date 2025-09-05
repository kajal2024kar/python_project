import pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Freehand Drawing with Mouse")
font = pygame.font.SysFont(None, 20)

def draw_button(window , colour, button_rect, text="Click me"):
    pygame.draw.rect(window, colour, button_rect, border_radius=10)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=button_rect.center)
    window.blit(text_surface, text_rect)
red_button = pygame.Rect(0,0,50,50)
# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DRAW_COLOR = BLACK

# Fill background
win.fill(WHITE)

# Variables
drawing = False
last_pos = None
brush_size = 5

# Main loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # Start drawing on mouse down
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            last_pos = event.pos

        # Stop drawing on mouse up
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            last_pos = None

        # Mouse motion with button held down
        if event.type == pygame.MOUSEMOTION and drawing:
            pygame.draw.line(win, DRAW_COLOR, last_pos, event.pos, brush_size)
            last_pos = event.pos
    draw_button(win,'red',red_button,"RED")
    pygame.display.update()

pygame.quit()
