import pygame,random


pygame.init()
FPS = 60

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 4, 4

RECT_HEIGHT = HEIGHT // ROWS
RECT_WIDTH = WIDTH // COLS

OUTLINE_COLOR = (187, 173, 160)
OUTLINE_THICKNESS = 10
BACKGROUND_COLOR = (205, 192, 180)
FONT_COLOR = (119, 110, 101)

FONT = pygame.font.SysFont("comicsans", 60, bold=True)
MOVE_VEL = 20

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")
clock = pygame.time.Clock()

#the tile object
class Tile:
    tile_colors = {
        0: (205, 193, 180), 2: (238, 228, 218), 4: (237, 224, 200),
        8: (242, 177, 121), 16: (245, 149, 99), 32: (246, 124, 95),
        64: (246, 94, 59), 128: (237, 207, 114), 256: (237, 204, 97),
        512: (237, 200, 80), 1024: (237, 197, 63), 2048: (237, 194, 46),
        'super': (60, 58, 50)
    }

    tile_text_colors = {
        0: (119, 110, 101), 2: (119, 110, 101), 4: (119, 110, 101),
        8: (249, 246, 242), 16: (249, 246, 242), 32: (249, 246, 242),
        64: (249, 246, 242), 128: (249, 246, 242), 256: (249, 246, 242),
        512: (249, 246, 242), 1024: (249, 246, 242), 2048: (249, 246, 242),
        'super': (249, 246, 242)
    }

    def __init__(self, value, row, col):
        self.value = value
        self.row = row
        self.col = col
        self.x = col * RECT_WIDTH
        self.y = row * RECT_HEIGHT

    def get_colour(self):
        colour = Tile.tile_colors.get(self.value, Tile.tile_colors['super'])
        text_c = Tile.tile_text_colors.get(self.value, Tile.tile_text_colors['super'])
        return colour, text_c

    def draw(self, window):
        colour, text_colour = self.get_colour()
        pygame.draw.rect(window, colour, (self.x, self.y, RECT_WIDTH, RECT_HEIGHT))
        if self.value != 0:
            text = FONT.render(str(self.value), True, text_colour)
            text_rect = text.get_rect(center=(self.x + RECT_WIDTH // 2, self.y + RECT_HEIGHT // 2))
            window.blit(text, text_rect)

def draw_grid(window):
    for row in range(ROWS):
        for col in range(COLS):
            x = col * RECT_WIDTH
            y = row * RECT_HEIGHT
            pygame.draw.rect(window, OUTLINE_COLOR, (x, y, RECT_WIDTH, RECT_HEIGHT), OUTLINE_THICKNESS)

#the tiles dwowing
def get_random(tiles):
    row ,col = None,None
    while True:
        row = random.randrange(0,ROWS)
        col = random.randrange(0,COLS)
        if f"{row}{col}" not in tiles:
            break
    return row,col
def genarte_tile():
     tiles = {}
     for _ in range(2):
         row,col = get_random(tiles)
         tiles[f"{row}{col}"] = Tile(2,row,col)
     return tiles


def draw(window, tiles):
    window.fill(BACKGROUND_COLOR)
    for tile in tiles.values():
        tile.draw(window)
    draw_grid(window)
    pygame.display.update()

def main(win):
    RUN = True

    tiles = genarte_tile()

    while RUN:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False

        draw(WINDOW, tiles)
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main(WINDOW)
