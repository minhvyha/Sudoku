import pygame
from board import Board
import time
from button import Button

# initialize pygame library
pygame.init() 

pygame.display.set_caption('Sudoku')

# Window set up
WIDTH = 700
HEIGHT = 700
BOARD_WIDTH = 500
BOARD_HEIGHT = 500

# Board
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

RED = (255, 0, 0)
GREEN = (60, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 120)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (180, 180, 180)
DGREY = (75, 75, 75)
TURQUOISE = (64, 224, 208)


FONT = pygame.font.SysFont('comicsans', 30)

# Start button
easy_button = Button(WIN, (DGREY), GREEN, WIDTH // 2, 180, 200, 70, 'Easy')
medium_button = Button(WIN, (DGREY), ORANGE, WIDTH // 2, 270, 200, 70, 'Medium')
hard_button = Button(WIN, (DGREY), RED, WIDTH // 2, 360, 200, 70, 'Hard')

# In-game button
new = Button(WIN, (WHITE), BLACK, BOARD_WIDTH + 100, 540, 150, 60, 'New Game')
check = Button(WIN, (WHITE), BLACK, BOARD_WIDTH + 100, 625, 150, 60, 'Check')

BACKGROUND = pygame.image.load('assets/start.png')

# Set up the board
BOARD = Board(WIN, BOARD_WIDTH, BOARD_HEIGHT, WIDTH - BOARD_WIDTH)

FPS = 30
MODE = None
ERROR = 0


def main():
    isSleep = False
    isRun = True
    isStart = False
    clock = pygame.time.Clock()
    # Loop forever to draw up the window every second
    while isRun:
        
        # Get any event from user such as mouse click, key pressed
        clock.tick(FPS)
        mouse = pygame.mouse.get_pos()
        # pygame.event.get() = [click (50, 100)]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRun = False
                break
            
            keys = pygame.key.get_pressed()

            if (BOARD.curr != None) and (keys) and isStart:
                assign(keys)

            if pygame.mouse.get_pressed()[0]:
                
                if not isStart:
                    if easy_button.isOver(mouse):
                        MODE = 23
                        isStart = True
                    elif medium_button.isOver(mouse):
                        MODE = 20
                        isStart = True
                    elif hard_button.isOver(mouse):
                        MODE = 17
                        isStart = True
                    if MODE:
                        BOARD.MakeSudoku(MODE)
                    continue
                
                x, y = mouse
                if x < BOARD_WIDTH - 5 and y > WIDTH - BOARD_WIDTH - 2 and y < WIDTH - 5:
                    BOARD.select(x, y)
                    isSleep = True
                else:
                    if new.isOver(mouse):
                        BOARD.MakeSudoku(MODE)
        if not isStart:
            draw_start()
            continue
        draw()
        if isSleep:
            isSleep = False
            time.sleep(0.2)
    pygame.quit()


# keys = [1]
def assign(keys):
    global ERROR
    if keys[pygame.K_1]:
        ERROR += BOARD.assign(1)
    elif keys[pygame.K_2]:
        ERROR += BOARD.assign(2) 
    elif keys[pygame.K_3]:
        ERROR += BOARD.assign(3)
    elif keys[pygame.K_4]:
        ERROR += BOARD.assign(4)
    elif keys[pygame.K_5]:
        ERROR += BOARD.assign(5)
    elif keys[pygame.K_6]:
        ERROR += BOARD.assign(6)
    elif keys[pygame.K_7]:
        ERROR += BOARD.assign(7)
    elif keys[pygame.K_8]:
        ERROR += BOARD.assign(8)
    elif keys[pygame.K_9]:
        ERROR += BOARD.assign(9)


#Function to draw the window
def draw():
      
    
    # Make changes to the window
    WIN.fill((WHITE))


    if BOARD.curr:
        row, col = BOARD.curr

        hor = pygame.Surface((500,500 // 9))
        ver = pygame.Surface((500 // 9,500))
        box = pygame.Surface((500 // 3, 500 // 3))

        box.set_alpha(80)
        box.fill((200, 230, 255))

        hor.set_alpha(80)
        hor.fill((197,226,255))   
        
        ver.set_alpha(80)
        ver.fill((197,226,255)) 
        
        box_col = col //3
        box_row = row // 3
        WIN.blit(box, (BOARD_WIDTH // 3 * box_col, + BOARD_WIDTH // 3 * box_row + WIDTH - BOARD_WIDTH))
        WIN.blit(ver, (BOARD_WIDTH // 9 * col + 2.5, WIDTH - BOARD_WIDTH))
        WIN.blit(hor, (0, BOARD_WIDTH // 9 * row + WIDTH - BOARD_WIDTH + 3))
    BOARD.draw()
    error = FONT.render(f'Error: {ERROR}', 1, BLACK)
    new.draw(BLACK)
    check.draw(BLACK)
    WIN.blit(error, (10, 10))


    


    # Update and display all the changes
    pygame.display.update()


def draw_start():
    WIN.blit(BACKGROUND, (0, 0))

    easy_button.draw()
    medium_button.draw()
    hard_button.draw()


    pygame.display.update()


def lose():
    draw()


# Execute all the code
if __name__ == '__main__':
    main()
    