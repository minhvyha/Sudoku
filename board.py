import pygame
import random
import time


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
BLUE_TEXT = (4,116,227)



# Font
FONT = pygame.font.SysFont('arial', 25)


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
        self.draw_same()
        self.error()
        self.draw_select()
        self.draw_grid()
        self.draw_board()
     
    

    def MakeSudoku(self, difficulty, isDraw):
        self.makeBoard(difficulty, isDraw)
        while not self.solveSudoku(False):
            self.makeBoard(difficulty, isDraw)
        self.default()
    
    def makeBoard(self, difficulty, isDraw):
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
            if isDraw:
                time.sleep(0.0001)
                self.WIN.fill((255, 255, 255))
                self.draw_grid()
                self.draw_board()
                pygame.display.update()

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
            self.board[row][col].value = value
            return 1
        self.board[row][col].value = value
        self.board[row][col].error = None
        return 0

    def reset(self):
        for i in self.board:
            for j in i:
                j.lock = False
                j.value = 0

    def draw_same(self):
        if self.curr != None:
            row, col = self.curr
            y = row * (self.height // 9) + self.padding + row * 0.45
            x = col * (self.width // 9) + col * 0.45
            box = pygame.Surface((500 // 9 + 1,500 // 9 + 1))
            box.set_alpha(200)
            box.fill((175,205,255))

            if self.board[row][col].value != 0:
                value = self.board[row][col].value
                for i, row in enumerate(self.board):
                    for j, block in enumerate(row):
                        if block.value == value:
                            x = j * (self.width // 9) + j * 0.45
                            y = i * (self.height // 9) + self.padding + i * 0.45
                            self.WIN.blit(box, (x, y))

    def draw_select(self):
        if self.curr != None:
            row, col = self.curr
            y = row * (self.height // 9) + self.padding + row * 0.45
            x = col * (self.width // 9) + col * 0.45
            box = pygame.Surface((500 // 9 + 1,500 // 9 + 1))
            box.set_alpha(300)
            box.fill((188,222,251))
            self.WIN.blit(box, (x, y))

    def error(self):
            white_box = pygame.Surface((500 // 9 + 1,500 // 9 + 1))
            white_box.set_alpha(500)
            white_box.fill((255,255,255))

            box = pygame.Surface((500 // 9 + 1,500 // 9 + 1))
            box.set_alpha(50)
            box.fill((235,0,0)) 

            for i, row in enumerate(self.board):
                for j, block in enumerate(row):
                    if block.error:
                        x = j * (self.width // 9) + j * 0.45
                        y = i * (self.height // 9) + self.padding + i * 0.45
                        self.WIN.blit(white_box, (x, y))
                        self.WIN.blit(box, (x, y))
            
    def draw_board(self):
        for i in self.board:
            for j in i:
                j.draw()

    def draw_grid(self):
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

    def solveSudoku(self, isDraw):
        empty = 0
        for i in self.board:
            for j in i:
                if j.value == 0:
                    empty += 1
        return self.solution(isDraw, empty)

        
    def solution(self, isDraw, empty, row=0, col=0):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        if empty == 0:
            return True
        if self.board[row][col].value != 0:
            if self.solution(isDraw ,empty, row=row + 1 if col == 8 else row, col=col + 1 if col != 8 else 0):
                return True
            return False

        for i in range(1, 10):
            if self.CheckValid(row, col, i):
                self.board[row][col].value = i
                if isDraw:
                    time.sleep(0.03)
                    self.WIN.fill((255, 255, 255))
                    self.draw_grid()
                    self.draw_board()
                    pygame.display.update()
                if self.solution(isDraw ,empty - 1, row=row + 1 if col == 8 else row, col=col + 1 if col != 8 else 0):
                    return True
        self.board[row][col].value = 0
        return False

    def default(self):
        for i in self.board:
            for j in i:
                if not j.lock:
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
        if self.lock:
            color = BLACK
        elif self.error == self.value:
            color = RED
        else:
            color = BLUE_TEXT
        if self.value != 0:
            num = FONT.render(f'{self.value}', 1, color)
            self.WIN.blit(num, (self.width // 9 * self.row + (self.width // 9 // 2) - num.get_width() // 2 + self.row * 0.55, self.padding + (self.height // 9) * self.col + self.height // 9 // 2 - num.get_height() // 2 + self.col * 0.55))


