
from constants import SQUARE_SIZE, RED, WHITE, BLACK, GREY, CROWN
import pygame

class Piece:
    #constants
    PADDING = 8
    OUTLINE = 1

    #attributes
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.calc_pos()
        self.movable = True

    #methods
    #placing pieces on the board
    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def draw(self, win):
        radius = SQUARE_SIZE // 2 - self.PADDING
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        #draws crown if the piece is a king
        if self.king:
            win.blit(CROWN, (self.x - CROWN.get_width() // 2, self.y - CROWN.get_height() // 2 - 15))

    def make_king(self):
        self.king = True

    #movement of the piece
    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()
    
    def __repr__(self):
        return str(self.color)

