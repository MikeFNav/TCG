
#handels the game logic and if pieces can move or not
import pygame
from classes.board import Board
from classes.player import player
from constants import GREY, RED, BLUE, SQUARE_SIZE, BLACK, WIDTH, HEIGHT, game_font


class Game:
    #attributes
    def __init__(self, win):
        self._init()
        self.win = win

    def _init(self):
            self.selected = None
            self.board = Board()
            self.playerR = player(RED)
            self.playerB = player(BLUE)
            self.playerR.points = 10
            self.playerB.points = 10
            self.turn = RED
            self.valid_moves = {}

    #methods
    def reset(self):
           self._init()

    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        self.update_points()
        pygame.display.update()


    #if something is seleted, try to move it to the new position
    #if it doesnt work, deselect the piece and try to select the new one again
    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                piece = self.board.get_piece(row, col)
                if piece != 0 and piece.color == self.turn:
                    self.selected = piece
                    self.valid_moves = self.board.get_valid_moves(piece)
                    return True
#                self.selected = None
#                self.select(row, col)
            return False
        
        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True
        return False

    def draw_valid_moves(self, moves):
            for move in moves:
                row, col = move
                pygame.draw.circle(self.win, GREY, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 8)

    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and (row, col) in self.valid_moves:
            skipped = self.valid_moves[(row, col)]
            if self.turn == RED:
                self.playerR.points -= 1
            else:
                self.playerB.points -= 1
            if skipped:
                self.board.remove(skipped) #removes enemy piece first
            self.board.move(self.selected, row, col) # then moves into empty square
            self.change_turn()
        else:
            return False
        return True

    def change_turn(self):
        self.valid_moves = {}
        if self.turn == RED:
            self.turn = BLUE
            self.playerR.points += 1
            print("Player 1 points: ", self.playerR.points) #testing, worked yay
        else:
            self.turn = RED
            self.playerB.points += 1

    def update_points(self):
        text_pointsR = str(self.playerR.points)
        text_pointsB = str(self.playerB.points)
        text_surfaceR = game_font.render(text_pointsR, False, BLACK)
        text_surfaceB = game_font.render(text_pointsB, False, BLACK)
        self.win.blit(text_surfaceR, (WIDTH - SQUARE_SIZE + 10, 8))
        self.win.blit(text_surfaceB, (WIDTH - SQUARE_SIZE + 10, HEIGHT - 8*SQUARE_SIZE + 8))

    def winner(self):
        return self.board.winner()

