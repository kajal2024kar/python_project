import pygame
import random

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini RPG Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (50, 200, 50)
RED = (200, 50, 50)
BLUE = (50, 50, 200)

# Player settings
player_size = 40
player = pygame.Rect(100, 100, player_size, player_size)
player_speed = 5

# Enemy settings
enemy_size = 40
enemy = pygame.Rect(400, 300, enemy_size, enemy_size)

# Clock
clock = pygame.time.Clock()

# Font
font = pygame.font.SysFont(None, 36)

# Battle state
in_battle = False
player_hp = 100
enemy_hp = 50

# Game loop
running = True
while running:
    screen.fill(GREEN)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if not in_battle:
        if keys[pygame.K_LEFT]:
            player.x -= player_speed
        if keys[pygame.K_RIGHT]:
            player.x += player_speed
        if keys[pygame.K_UP]:
            player.y -= player_speed
        if keys[pygame.K_DOWN]:
            player.y += player_speed

        # Enemy random movement
        enemy.x += random.choice([-2, -1, 0, 1, 2])
        enemy.y += random.choice([-2, -1, 0, 1, 2])

        # Collision detection
        if player.colliderect(enemy):
            in_battle = True

    else:
        screen.fill(WHITE)
        battle_text = font.render("Battle! Press SPACE to Attack", True, RED)
        screen.blit(battle_text, (200, 200))

        hp_text = font.render(f"Player HP: {player_hp}  Enemy HP: {enemy_hp}", True, BLUE)
        screen.blit(hp_text, (200, 300))

        if keys[pygame.K_SPACE]:
            damage = random.randint(5, 20)
            enemy_hp -= damage
            if enemy_hp <= 0:
                in_battle = False
                enemy_hp = 50
                enemy.x, enemy.y = random.randint(100, 700), random.randint(100, 500)

    # Draw characters
    if not in_battle:
        pygame.draw.rect(screen, BLUE, player)
        pygame.draw.rect(screen, RED, enemy)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
