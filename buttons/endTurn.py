
import pygame
from constants import BLACK, BLUE, SQUARE_SIZE, WIDTH, GREY, game_font, HEIGHT


class end_turn_button:
    def __init__(self, win):
        self.win = win
        self.draw_end_turn_button()
                    
    def draw_end_turn_button(self):
            text_EndTurn = str("End Turn")
            text_surface_EndTurn = game_font.render(text_EndTurn, False, BLACK)
            self.win.blit(text_surface_EndTurn, (WIDTH - 4*SQUARE_SIZE +4, HEIGHT - 8.5*SQUARE_SIZE + 8))
