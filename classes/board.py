
import pygame
from constants import BLACK, HEIGHT, LIGHT_GREY, ROWS, COLS, RED, WHITE, BLUE, SQUARE_SIZE, WIDTH, GREY
from .piece import Piece
from buttons.endTurn import end_turn_button
OUTLINE = 2

class Board:
    #atributes
    def __init__(self):
        self.board = []
        self.red_left = self.blue_left = 12
        self.red_kings = self.blue_kings = 0
        self.create_board()

    #methods
    #creating the board 
    def draw_squares(self, win):
        win.fill(LIGHT_GREY)
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(win, WHITE, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    
    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):
                    if row < 3 and col < 16:
                        self.board[row].append(Piece(row, col, RED))  # Red piece
                    elif row > 12 and col < 16:
                        self.board[row].append(Piece(row, col, BLUE))  # Blue piece
                    else:
                        self.board[row].append(0)  # Empty square
                else:
                    self.board[row].append(0)  # Empty square
        self.board[12][9] = Piece(12, 9, RED) # adds red piece at the bottom to test the kinging feature

    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.calc_pos()
                    piece.draw(win)
        pygame.draw.line(win, BLACK, (16 * SQUARE_SIZE, 0), (16 * SQUARE_SIZE, HEIGHT), 2)  # Vertical line to separate board from side panel
        pygame.draw.line(win, BLACK, (22 * SQUARE_SIZE, HEIGHT // 2), (16 * SQUARE_SIZE, HEIGHT // 2), 2)
        pygame.draw.rect(win, BLACK, (18 * SQUARE_SIZE -2, 7.5 * SQUARE_SIZE -2, 2 * SQUARE_SIZE + 2*OUTLINE, SQUARE_SIZE + 2*OUTLINE))
        pygame.draw.rect(win, WHITE, (18 * SQUARE_SIZE, 7.5 * SQUARE_SIZE, 2 * SQUARE_SIZE, SQUARE_SIZE))
        end_turn_button(win)

    #movement of the pieces
    #making the king
    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

        if row == ROWS -1 and piece.color == RED or row == 0 and piece.color == BLUE:
            piece.make_king()
            if piece.color == BLUE:
                self.blue_kings += 1
            else:
                self.red_kings += 1

    #not sure
    def get_piece(self, row, col):
        return self.board[row][col]

    #getting valid moves for the pieces based on direction they can go in
    def get_valid_moves(self, piece):
        moves = {}
        directions = [
            (-1, 0), #up
            (1, 0),  #down
            (0, -1), #left
            (0, 1)]  #right
        moves = self.get_valid_moves_init(piece, directions, moves)

        if piece.king:
            directions = [
                (-2, 0), #up2
                (2, 0),  #down2
                (0, -2), #left2
                (0, 2)]  #right2
            moves = self.get_valid_moves_init(piece, directions, moves)

        return moves

    #repeated code, gets valid moves for pieces no matter what dirrection they can travel
    def get_valid_moves_init(self, piece, directions, moves):
        for d_row, d_col in directions:
            new_row = piece.row + d_row
            new_col = piece.col + d_col

            if 0 <= new_row < ROWS and 0 <= new_col < COLS - 6:
                target_piece = self.get_piece(new_row, new_col)

                if target_piece == 0:
                    moves[(new_row, new_col)] = []
                elif target_piece.color != piece.color:
                    moves[(new_row, new_col)] = [target_piece]
        return moves

    #removes the piece that we land on (skipped)
    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color == RED:
                    self.red_left -= 1
                else:
                    self.blue_left -= 1

    def winner(self):
        if self.red_left <= 0:
            return BLUE
        elif self.blue_left <= 0:
            return RED
        return None


        

    
