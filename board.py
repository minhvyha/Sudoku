import pygame
pygame.init()

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



class Board:
    def __init__(self, WIN, width, height) -> None:
        # 9 x 9 sudoku board
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        # Get the reference for the window
        self.WIN = WIN
        self.width = width
        self.height = height

    # Draw the board into the window
    def draw(self) -> None:
        for i in range(9):
            thickness = 1
            if (i) % 3 == 0:
                thickness = 3
            pygame.draw.line(self.WIN, DGREY, (0, i * self.height / 9), (self.width, i * self.height / 9), thickness)
        for i in range(9):
            thickness = 1
            if (i) % 3 == 0:
                thickness = 3
            pygame.draw.line(self.WIN, DGREY, (i * self.width / 9, 0), (i * self.width / 9, self.height), thickness)

class Block:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def draw(self):
        pass
