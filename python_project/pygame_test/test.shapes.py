import pygame
pygame.init()

# Set up window
win = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Drawing in Pygame")

# Colors
WHITE = (255, 255, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)
BLACK = (0, 0, 0)

run = True
while run:
    win.fill(WHITE)  # Clear screen

    # Draw shapes
    pygame.draw.line(win, RED, (50, 50), (200, 50), 2)
    pygame.draw.rect(win, GREEN, (100, 100, 150, 100))  # x, y, width, height
    pygame.draw.circle(win, BLUE, (400, 300), 60)       # center_x, center_y, radius
    pygame.draw.ellipse(win, RED, (300, 400, 150, 80))  # bounding box
    pygame.draw.polygon(win, BLACK, [(600, 100), (700, 200), (500, 200)])

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
