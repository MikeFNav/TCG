
import pygame

WIDTH, HEIGHT = 968, 704
ROWS, COLS = 16, 22
SQUARE_SIZE = WIDTH//COLS
OUTLINE_SIZE_COLS = WIDTH//(COLS)

#RGB colours
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)
LIGHT_GREY = (240, 240, 240)

#fonts
pygame.font.init()
game_font = pygame.font.SysFont("Arial", 24)

#assets
CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (25, 14))



