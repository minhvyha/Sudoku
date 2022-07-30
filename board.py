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
        self.curr = None

    # Draw the board into the window
    def draw(self) -> None:
        if self.curr != None:
            row, col = self.curr
            y = row * (self.height // 9) + self.padding + row * 0.35
            x = col * (self.width // 9) + col * 0.35
            box = pygame.Surface((500 // 9 + 1,500 // 9 + 1))
            box.set_alpha(200)
            box.fill((175,205,255))
            self.WIN.blit(box, (x, y))
            if self.board[row][col].value != 0:
                value = self.board[row][col].value
                for i, row in enumerate(self.board):
                    for j, block in enumerate(row):
                        if block.value == value:
                            x = j * (self.width // 9) + j * 0.3
                            y = i * (self.height // 9) + self.padding + i * 0.3
                            self.WIN.blit(box, (x, y))


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

        

        
    def MakeSudoku(self, difficulty):
        self.reset()
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
            self.board[row][col].lock = True

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
    
    def select(self, x, y):
        row = (y - self.padding) // (self.height // 9)
        col = x // (self.width // 9)
        self.curr = (row, col)

    
    def assign(self, value):
        row, col = self.curr
        if self.board[row][col].lock:
            return 0
        if self.board[row][col].value == value:
            return 0
        if not self.CheckValid(row, col, value):
            if self.board[row][col].error == value:
                return 0
            self.board[row][col].error = value
            return 1
        self.board[row][col].value = value
        return 0

    def reset(self):
        for i in self.board:
            for j in i:
                j.value = 0


class Block:
    def __init__(self, WIN, row, col, width, height, padding, lock=False):
        self.padding = padding
        self.width = width
        self.height = height
        self.WIN = WIN
        self.row = row
        self.col = col
        self.value = 0
        self.lock = lock
        self.error = None

    def draw(self):
        if self.value != 0:
            num = FONT.render(f'{self.value}', 1, BLACK)
            self.WIN.blit(num, (self.width // 9 * self.row + (self.width // 9 // 2) - num.get_width() // 2, self.padding + (self.height // 9) * self.col + self.height // 9 // 2 - num.get_height() // 2))