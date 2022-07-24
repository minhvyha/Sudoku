import pygame
import random

pygame.init()



# Color
RED = (255, 0, 0)
GREEN = (60, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 120)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (180, 180, 180)
DGREY = (50, 50, 50)
TURQUOISE = (64, 224, 208)



# Difficulty

EASY = 28
MEDIUM = 22
HARD = 17
# Font
FONT = pygame.font.SysFont('comicsans', 25)


# An object 
class Board:
    def __init__(self, WIN, width, height, padding) -> None:
        # 9 x 9 sudoku board
        self.board = [[Block(WIN, row, col, width, height, padding) for row in range(9)]for col in range(9)]
        # Get the reference for the window
        self.WIN = WIN
        self.width = width
        self.height = height
        self.padding = padding

        self.MakeSudoku()

    # Draw the board into the window
    def draw(self) -> None:

        # Draw row
        for i in range(10):
            thickness = 1
            if (i) % 3 == 0:
                thickness = 3
            pygame.draw.line(self.WIN, DGREY, (0, i * self.height // 9 + self.padding), (self.width, i * self.height // 9 + self.padding), thickness)
        # (Window, color, starting position in (x, y), ending pos in x, y, thickness)

        # Draw col
        for i in range(10):
            thickness = 1
            if (i) % 3 == 0:
                thickness = 3
            pygame.draw.line(self.WIN, DGREY, (i * self.width // 9, self.padding), (i * self.width // 9, self.height + self.padding), thickness)

        for i in self.board:
            for j in i:
                j.draw()
        
    def MakeSudoku(self):
        difficulty = MEDIUM
        for i in range(difficulty):
            #choose random numbers
            row = random.randrange(9)
            col = random.randrange(9)
            num = random.randrange(1, 10)

            while self.CheckValid(row, col, num) == False or self.board[row][col].value != 0: # if taken or not valid reroll
                row = random.randrange(9)
                col = random.randrange(9)
                num = random.randrange(1, 10)
            self.board[row][col].value = num

    def CheckValid(self, row, col, num):

        for x in range(9):
            if self.board[x][col].value == num:
                return False
                
        for y in range(9):
            if self.board[row][y].value == num:
                return False

        rowsection = row // 3
        colsection = col // 3

        for x in range(3):
            for y in range(3):
                if self.board[rowsection * 3 + x][colsection * 3 + y].value == num:
                    return False
        return True


class Block:
    def __init__(self, WIN, row, col, width, height, padding):
        self.padding = padding
        self.width = width
        self.height = height
        self.WIN = WIN
        self.row = row
        self.col = col
        self.value = 0

    def draw(self):
        if self.value != 0:
            num = FONT.render(f'{self.value}', 1, BLACK)
            self.WIN.blit(num, (self.width // 9 * self.row + (self.width // 9 // 2) - num.get_width() // 2, self.padding + (self.height // 9) * self.col + self.height // 9 // 2 - num.get_height() // 2))