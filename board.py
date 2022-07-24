import pygame

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
        if self.value != -1:
            num = FONT.render(f'{self.value}', 1, BLACK)
            self.WIN.blit(num, (self.width // 9 * self.row + (self.width // 9 // 2) - num.get_width() // 2, self.padding + (self.height // 9) * self.col + self.height // 9 // 2 - num.get_height() // 2))
    


import random
 
def MakeSudoku():
    Grid = [[0 for x in range(9)] for y in range(9)]
            
    for i in range(9):
        for j in range(9):
            Grid[i][j] = 0
            
    # The range here is the amount
    # of numbers in the grid
    for i in range(17):
        #choose random numbers
        row = random.randrange(9)
        col = random.randrange(9)
        num = random.randrange(1,10)
        while(not CheckValid(Grid,row,col,num) or Grid[row][col] != 0): #if taken or not valid reroll
            row = random.randrange(9)
            col = random.randrange(9)
            num = random.randrange(1,10)
        Grid[row][col]= num;
        
    Printgrid(Grid)

    #check to see whether the number is valid
def CheckValid(Grid,row,col,num):
    #check if in row
    valid = True
    #check row and collumn
    for x in range(9):
        if (Grid[x][col] == num):
            valid = False
    for y in range(9):
        if (Grid[row][y] == num):
            valid = False
    rowsection = row // 3
    colsection = col // 3
    for x in range(3):
        for y in range(3):
            #check if section is valid
            if(Grid[rowsection*3 + x][colsection*3 + y] == num):
                valid = False
    return valid
 
 
def Printgrid(Grid):
    TableTB = "|--------------------------------|"
    TableMD = "|----------+----------+----------|"
    print(TableTB)
    for x in range(9):
        for y in range(9):
            if ((x == 3 or x == 6) and y == 0):
                print(TableMD)
            if (y == 0 or y == 3 or y== 6):
                print("|", end=" ")
            print(" " + str(Grid[x][y]), end=" ")
            if (y == 8):
                print("|")
    print(TableTB)

    

 
MakeSudoku()